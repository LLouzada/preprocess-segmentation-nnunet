import os
import glob
from random import shuffle
import re
import cv2
import src.constants as cons
import numpy as np
import matplotlib.pyplot as plt

def visualize_all(n="5", is_overlay=False, is_shuffle=True):
    dir_name = cons.RESULT_DIR
    path = os.path.join(dir_name, 'result002', 'imagesTs', '*.png')
    img_files = glob.glob(path)
    if not img_files:
        print(f"No images found in {dir_name}.")
        return
    if is_shuffle:
        shuffle(img_files)
    og_mask_files = [replace_last_0000(img.replace('imagesTs', 'labelsTs')) for img in img_files]
    if not og_mask_files:
        print(f"No og masks found in {dir_name}.")
        return
    predicted_mask_files = [replace_last_0000(img.replace('imagesTs', 'result2')) for img in img_files]
    if not predicted_mask_files:
        print(f"No predicted masks found in {dir_name}.")
        return
    pp_predicted_mask_files = [replace_last_0000(img.replace('imagesTs', 'result2_pp')) for img in img_files]
    if not pp_predicted_mask_files:
        print(f"No post-processed predicted masks found in {dir_name}.")
        return
    if not n == "all":
        n = int(n)
    else:
        assert n == "all", "Invalid value for --n argument"
        n = len(img_files)
    
    image_dataset = []
    og_mask_dataset = []
    predicted_mask_dataset = []
    pp_predicted_mask_dataset = []

    for img, og_mask, predicted_mask, pp_predicted_mask in zip(img_files, og_mask_files, predicted_mask_files, pp_predicted_mask_files):
        img_arr = cv2.imread(img, cv2.IMREAD_GRAYSCALE)
        mask_arr = cv2.imread(og_mask, cv2.IMREAD_GRAYSCALE)
        predicted_mask_arr = cv2.imread(predicted_mask, cv2.IMREAD_GRAYSCALE)
        pp_predicted_mask_arr = cv2.imread(pp_predicted_mask, cv2.IMREAD_GRAYSCALE)

        image_dataset.append(img_arr)
        og_mask_dataset.append(mask_arr)
        predicted_mask_dataset.append(predicted_mask_arr)
        pp_predicted_mask_dataset.append(pp_predicted_mask_arr)

    image_dataset = np.array(image_dataset)
    og_mask_dataset = np.array(og_mask_dataset)
    predicted_mask_dataset = np.array(predicted_mask_dataset)
    pp_predicted_mask_dataset = np.array(pp_predicted_mask_dataset)

    print("Image name: ", img_files[0])
    print("Mask name: ", og_mask_files[0])
    print("Predicted mask name: ", predicted_mask_files[0])
    print("Post-processed predicted mask name: ", pp_predicted_mask_files[0])
    print("Image directory: ", dir_name)
    print("Shape of image dataset: ", image_dataset.shape)
    print("Shape of mask dataset: ", og_mask_dataset.shape)
    print("Shape of predicted mask dataset: ", predicted_mask_dataset.shape)
    print("Shape of post-processed predicted mask dataset: ", pp_predicted_mask_dataset.shape)
    print()

    for i in range(min(n, len(image_dataset))):
        fig, axes = plt.subplots(1, 4, figsize=(20, 5))
        
        # Image
        axes[0].imshow(image_dataset[i], cmap='gray')
        axes[0].set_title('Image ' + img_files[i].split('/')[-1].split('.')[0])
        
        # Original Mask
        axes[1].imshow(og_mask_dataset[i], cmap='gray')
        axes[1].set_title('Original Mask')
        
        # Predicted Mask
        axes[2].imshow(predicted_mask_dataset[i], cmap='gray')
        axes[2].set_title('Predicted Mask')
        
        # Post-Processed Predicted Mask
        axes[3].imshow(pp_predicted_mask_dataset[i], cmap='gray')
        axes[3].set_title('PP Predicted Mask')
        
        # Maximize the figure window
        manager = plt.get_current_fig_manager()
        manager.window.showMaximized()
        # Show the plot
        plt.tight_layout()
        plt.show()


def replace_last_0000(s):
    return re.sub(r'(_0000)(?!.*_0000)', '', s)



def overlay_with_bounding_box(dir_name, n=5, is_overlay=False, result=2, is_shuffle=True):
    path = os.path.join(dir_name, 'result00' + str(result), 'imagesTs', '*.png')
    img_files = glob.glob(path)
    if not img_files:
        print(f"No images found in {path}.")
        return
    if is_shuffle:
        shuffle(img_files)
    if result == 1:
        mask_files = [replace_last_0000(img.replace('imagesTs', 'predicted')) for img in img_files]
    elif result == 2:
        mask_files = [replace_last_0000(img.replace('imagesTs', 'result2_pp')) for img in img_files]
    if not mask_files:
        print(f"No masks found in {dir_name}.")
        return
    
    image_dataset = []
    mask_dataset = []

    for img, mask in zip(img_files, mask_files):
        img_arr = cv2.imread(img, cv2.IMREAD_GRAYSCALE)
        mask_arr = cv2.imread(mask, cv2.IMREAD_GRAYSCALE)

        image_dataset.append(img_arr)
        mask_dataset.append(mask_arr)

    image_dataset = np.array(image_dataset)
    mask_dataset = np.array(mask_dataset)

    for i in range(min(n, len(image_dataset))):
        if not is_overlay:
            fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))
            ax1.imshow(image_dataset[i], cmap='gray')
            ax1.set_title('Image')
            ax2.imshow(mask_dataset[i], cmap='gray')
            ax2.set_title('Mask')
            plt.show()
        else:
            print("Image name: ", img_files[i])
            print("Mask name: ", mask_files[i])

            # Convert grayscale images to 3-channel images
            image1_colored = cv2.cvtColor(image_dataset[i], cv2.COLOR_GRAY2BGR)
            mask_colored = cv2.cvtColor(mask_dataset[i], cv2.COLOR_GRAY2BGR)

            # Color the mask region in green
            mask_2d = mask_dataset[i] == 255
            mask_colored[mask_2d, 0] = 0       # Red channel
            mask_colored[mask_2d, 1] = 255     # Green channel
            mask_colored[mask_2d, 2] = 0       # Blue channel

            # Overlay the images
            overlay = cv2.addWeighted(image1_colored, 0.7, mask_colored, 0.3, 0)

            # Find contours in the mask
            contours, _ = cv2.findContours(mask_dataset[i], cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

            if contours:
                print(f"Found {len(contours)} contours!")
                
                # Sort contours by area in descending order and pick the top 2
                sorted_contours = sorted(contours, key=cv2.contourArea, reverse=True)[:2]
                
                for contour in sorted_contours:
                    x, y, w, h = cv2.boundingRect(contour)
                    cv2.rectangle(overlay, (x, y), (x + w, y + h), (0, 255, 0), 2)  # Drawing in green color


            # Display the image with the file name (with out the full path)
            cv2.imshow(img_files[i].split('/')[-1], overlay)
            cv2.waitKey(0)
            cv2.destroyAllWindows()


def overlay_with_bounding_box_specific(dir_name, image_num, is_overlay=False, result=2, is_shuffle=True):
    path = os.path.join(dir_name, 'result00' + str(result), 'imagesTs', '*' + str(image_num) +'_0000.png')
    img_files = glob.glob(path)
    if not img_files:
        print(f"No images found in {path}.")
        return
    if is_shuffle:
        shuffle(img_files)
    if result == 1:
        mask_files = [replace_last_0000(img.replace('imagesTs', 'predicted')) for img in img_files]
    elif result == 2:
        mask_files = [replace_last_0000(img.replace('imagesTs', 'result2_pp')) for img in img_files]
    if not mask_files:
        print(f"No masks found in {dir_name}.")
        return
    
    image_dataset = []
    mask_dataset = []

    for img, mask in zip(img_files, mask_files):
        img_arr = cv2.imread(img, cv2.IMREAD_GRAYSCALE)
        mask_arr = cv2.imread(mask, cv2.IMREAD_GRAYSCALE)

        image_dataset.append(img_arr)
        mask_dataset.append(mask_arr)

    image_dataset = np.array(image_dataset)
    mask_dataset = np.array(mask_dataset)

    for i in range(min(1, len(image_dataset))):
        if not is_overlay:
            fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))
            ax1.imshow(image_dataset[i], cmap='gray')
            ax1.set_title('Image')
            ax2.imshow(mask_dataset[i], cmap='gray')
            ax2.set_title('Mask')
            plt.show()
        else:
            print("Image name: ", img_files[i])
            print("Mask name: ", mask_files[i])

            # Convert grayscale images to 3-channel images
            image1_colored = cv2.cvtColor(image_dataset[i], cv2.COLOR_GRAY2BGR)
            mask_colored = cv2.cvtColor(mask_dataset[i], cv2.COLOR_GRAY2BGR)

            # Color the mask region in green
            mask_2d = mask_dataset[i] == 255
            mask_colored[mask_2d, 0] = 0       # Red channel
            mask_colored[mask_2d, 1] = 255     # Green channel
            mask_colored[mask_2d, 2] = 0       # Blue channel

            # Overlay the images
            overlay = cv2.addWeighted(image1_colored, 0.7, mask_colored, 0.3, 0)

            # Find contours in the mask
            contours, _ = cv2.findContours(mask_dataset[i], cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

            if contours:
                print(f"Found {len(contours)} contours!")
                
                # Sort contours by area in descending order and pick the top 2
                sorted_contours = sorted(contours, key=cv2.contourArea, reverse=True)[:2]
                
                for contour in sorted_contours:
                    x, y, w, h = cv2.boundingRect(contour)
                    cv2.rectangle(overlay, (x, y), (x + w, y + h), (0, 255, 0), 2)  # Drawing in green color


            # Display the image with the file name (with out the full path)
            cv2.imshow(img_files[i].split('/')[-1], overlay)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
