import json
import os
import glob
import shutil
import src.constants as cons
from PIL import Image
from sklearn.model_selection import train_test_split

def collect_resized_images_and_masks(path):
    img_enum = "**/*_processed_resized.png"
    mask_enum = "**/*_mask_resized.png"
    
    img_files = list(glob.iglob(path + img_enum, recursive=True))
    mask_files = list(glob.iglob(path + mask_enum, recursive=True))
    
    # Filtering only valid pairs
    img_files = [img for img in img_files if img.replace('_processed_resized.png', '_mask_resized.png') in mask_files]
    mask_files = [img.replace('_processed_resized.png', '_mask_resized.png') for img in img_files]
    
    return img_files, mask_files

def save_to_directory(X, y, dir_name, prefix):
    i = 1
    for img, mask in zip(X, y):
        # Extract Positive or Negative from file path
        condition = 'Positive' if 'Positive' in img else 'Negative'
        
        # Construct new filenames
        new_img_name = "image_{}_{}_{}.png".format(prefix, condition.lower(), i)
        new_mask_name = "mask_{}_{}_{}.png".format(prefix, condition.lower(), i)
        
        shutil.copy(img, os.path.join(dir_name, 'images', new_img_name))
        shutil.copy(mask, os.path.join(dir_name, 'masks', new_mask_name))
        
        i += 1

def split_data(path):
    # Extract SPAIR or STIR from the path
    prefix = path.split('/')[-2].lower()

    # Collect resized images and masks
    image_dataset, mask_dataset = collect_resized_images_and_masks(path)

    # Split into train and test
    X_train, X_test, y_train, y_test = train_test_split(image_dataset, mask_dataset, test_size=0.20, random_state=42)

    # Create directories if they don't exist
    os.makedirs(os.path.join(cons.TRAIN_DIR, 'images'), exist_ok=True)
    os.makedirs(os.path.join(cons.TRAIN_DIR, 'masks'), exist_ok=True)
    os.makedirs(os.path.join(cons.TEST_DIR, 'images'), exist_ok=True)
    os.makedirs(os.path.join(cons.TEST_DIR, 'masks'), exist_ok=True)

    # Save the images and masks to respective directories
    save_to_directory(X_train, y_train, cons.TRAIN_DIR, prefix)
    save_to_directory(X_test, y_test, cons.TEST_DIR, prefix)


def organize_for_nnunet(input_dir=cons.TRAIN_DIR, test_dir=cons.TEST_DIR, output_dir=cons.NNUNET_DIR, dataset_name="SacroRM", dataset_id="002"):
    # Create folder structure
    dataset_folder = os.path.join(output_dir, f"Dataset{dataset_id}_{dataset_name}")
    imagesTr_folder = os.path.join(dataset_folder, "imagesTr")
    labelsTr_folder = os.path.join(dataset_folder, "labelsTr")
    imagesTs_folder = os.path.join(dataset_folder, "imagesTs")  
    labelsTs_folder = os.path.join(dataset_folder, "labelsTs")

    os.makedirs(imagesTr_folder, exist_ok=True)
    os.makedirs(labelsTr_folder, exist_ok=True)
    os.makedirs(imagesTs_folder, exist_ok=True)
    os.makedirs(labelsTs_folder, exist_ok=True)

    # Handling training images
    counter = 0
    for filename in os.listdir(os.path.join(input_dir, "images")):
        case_identifier = str(counter).zfill(4)
        modality_id = "0000"
        new_image_name = f"SRM_{case_identifier}_{modality_id}.png"
        shutil.copy(os.path.join(input_dir, "images", filename),
                    os.path.join(imagesTr_folder, new_image_name))
        
        mask_filename = filename.replace("image_", "mask_")
        new_mask_name = f"SRM_{case_identifier}.png"
        shutil.copy(os.path.join(input_dir, "masks", mask_filename),
                    os.path.join(labelsTr_folder, new_mask_name))

        counter += 1

    # Handling test images
    counter = 0
    for filename in os.listdir(os.path.join(test_dir, "images")):
        case_identifier = str(counter).zfill(3)
        modality_id = "0000"
        new_image_name = f"SRM_{case_identifier}_{modality_id}.png"
        shutil.copy(os.path.join(test_dir, "images", filename),
                    os.path.join(imagesTs_folder, new_image_name))
        tmask_filename = filename.replace("image_", "mask_")
        new_mask_name = f"SRM_{case_identifier}.png"
        shutil.copy(os.path.join(test_dir, "masks", tmask_filename),
                    os.path.join(labelsTs_folder, new_mask_name))

        counter += 1

    # Create dataset.json
    json_content = {
        "channel_names": {
            "R":"red",
            "G":"green",
            "B":"blue"
        },
        "labels": {
            "background": 0,
            "region_of_interest": 1
        },
        "numTraining": len(os.listdir(os.path.join(input_dir, "images"))),
        "file_ending": ".png",
        "overwrite_image_reader_writer": "NaturalImage2DIO"
    }

    with open(os.path.join(dataset_folder, "dataset.json"), 'w') as json_file:
        json.dump(json_content, json_file, indent=4)







