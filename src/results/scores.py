import os
import numpy as np
import cv2
import src.constants as cons
import glob

def dice_coefficient(img_path1, img_path2):
    y_true = cv2.imread(img_path1, cv2.IMREAD_GRAYSCALE)
    y_pred = cv2.imread(img_path2, cv2.IMREAD_GRAYSCALE)

    intersection = np.sum(y_true * y_pred)
    return (2. * intersection + 1e-5) / (np.sum(y_true) + np.sum(y_pred) + 1e-5)

def iou(img_path1, img_path2):
    y_true = cv2.imread(img_path1, cv2.IMREAD_GRAYSCALE)
    y_pred = cv2.imread(img_path2, cv2.IMREAD_GRAYSCALE)

    intersection = np.sum(y_true * y_pred)
    union = np.sum(y_true) + np.sum(y_pred) - intersection
    return (intersection + 1e-5) / (union + 1e-5)


def calculate_score(image_number, type):
    dir_name = cons.RESULT_DIR

    if not image_number == "all":
        is_all = False
        image_number_str = f"{int(image_number):03}"
        print("Image number: ", image_number_str)
        og_mask = os.path.join(dir_name, 'result002', 'labelsTs', 'SRM_' + image_number_str +'.png')
        og_mask_files = glob.glob(og_mask)
        if not og_mask_files:
            print("Og Mask not found")
            print("Og Mask path: ", og_mask_files)
            return
        predicted_mask = os.path.join(dir_name, 'result002', 'result2_pp', 'SRM_' + image_number_str +'.png')
        predicted_mask_files = glob.glob(predicted_mask)
        if not predicted_mask_files:
            print("Predicted Mask not found")
            print("Predicted Mask path: ", predicted_mask_files)
            return
    else:
        assert image_number == "all", "Invalid value for --n argument"
        is_all = True
        og_mask = os.path.join(dir_name, 'result002', 'labelsTs', '*.png')
        og_mask_files = glob.glob(og_mask)
        if not og_mask_files:
            print("Og Mask not found")
            print("Og Mask path: ", og_mask_files)
            return
        predicted_mask = og_mask.replace('labelsTs', 'result2_pp')
        predicted_mask_files = glob.glob(predicted_mask)
        if not predicted_mask_files:
            print("Predicted Mask not found")
            print("Predicted Mask path: ", predicted_mask_files)
            return
        
    
    print("Calculating score for image number: ", image_number)
    if type == 0:
        print("Selected score: Intersection over Union (IoU)")
    elif type == 1:
        print("Selected score: Dice Coefficient")
    elif type == 2:
        print("Selected score: Both")
    else:
        print("Invalid score type"
        "Please select one of the following options:"
        "iou - Intersection over Union"
        "dice - Dice Coefficient"
        "all - Both")
        return
    if not is_all:
        print("Original mask path: ", og_mask_files)
        print("Predicted mask path: ", predicted_mask_files)
    print("Number of images: ")
    print(" - Original ", len(og_mask_files))
    print(" - Predicted ", len(predicted_mask_files))
    
    if not is_all:
        if(type == 0 or type == 2):
            iou_score = iou(og_mask_files[0], predicted_mask_files[0])
            print(f"IoU: {iou_score:.4f}")
        if(type == 1 or type == 2):
            dice_score = dice_coefficient(og_mask_files[0], predicted_mask_files[0]) 
            print(f"Dice Coefficient: {dice_score:.4f}")
    else:
        # Calculate the mean score for all images
        iou_scores = []
        dice_scores = []

        for og_mask_file, predicted_mask_file in zip(og_mask_files, predicted_mask_files):
            if(type == 0 or type == 2):
                iou_score = iou(og_mask_file, predicted_mask_file)
                iou_scores.append(iou_score)
            if(type == 1 or type == 2):
                dice_score = dice_coefficient(og_mask_file, predicted_mask_file)
                dice_scores.append(dice_score)
            
        if(type == 0 or type == 2):
            print(f"Mean IoU: {np.mean(iou_scores):.4f}")
            print(f"Max IoU: {np.max(iou_scores):.4f}")
            print(f"Min IoU: {np.min(iou_scores):.4f}")
        if(type == 1 or type == 2):
            print(f"Mean Dice Coefficient: {np.mean(dice_scores):.4f}")
            print(f"Max Dice Coefficient: {np.max(dice_scores):.4f}")
            print(f"Min Dice Coefficient: {np.min(dice_scores):.4f}")



   

    

    

