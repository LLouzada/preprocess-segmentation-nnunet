import re
import cv2
import numpy as np
import os
import glob
import matplotlib.pyplot as plt
import src.constants as cons
from PIL import Image
from random import shuffle



def check_pairs(dir_name, size=cons.default_image_size):
    if dir_name == cons.NNUNET_DIR:
        img_files = glob.glob(os.path.join(dir_name, 'Dataset002_SacroRM', 'imagesTr', 'SRM_*_0000.png'))
        mask_files = [img.replace('imagesTr', 'labelsTr').replace('_0000', '') for img in img_files]
    else:
        img_files = glob.glob(os.path.join(dir_name, 'images', '*.png'))
        mask_files = glob.glob(os.path.join(dir_name, 'masks', '*.png'))
    

    # Checar se os números são iguais
    assert len(img_files) == len(mask_files), "Número de imagens e máscaras não é igual."

    # Checar pares por nome e dimensões das imagens
    for img, mask in zip(img_files, mask_files):  # Use zip to iterate over pairs
        base_name = os.path.basename(img)
        
        if dir_name == cons.NNUNET_DIR:
            corresponding_mask = mask  # masks are already matched in this case
        else:
            corresponding_mask = os.path.join(dir_name, 'masks', base_name.replace('image_', 'mask_'))
        
        assert os.path.exists(corresponding_mask), f"Máscara não encontrada para a imagem {base_name}"

        # Verificar o tamanho da imagem e da máscara
        img_arr = cv2.imread(img)
        mask_arr = cv2.imread(corresponding_mask, 0)
        assert img_arr.shape[0] == size and img_arr.shape[1] == size, f"A imagem {base_name} não tem as dimensões esperadas."
        assert mask_arr.shape[0] == size and mask_arr.shape[1] == size, f"A máscara {base_name.replace('image_', 'mask_')} não tem as dimensões esperadas."

    print(f"Todos os pares no diretório {dir_name} estão corretos e possuem as dimensões esperadas.")

def count_files(dir_name):
    if dir_name == cons.NNUNET_DIR:
        img_files = glob.glob(os.path.join(dir_name, 'Dataset002_SacroRM', 'imagesTr', '*.png'))
        mask_files = glob.glob(os.path.join(dir_name, 'Dataset002_SacroRM', 'labelsTr', '*.png'))
    else:
        img_files = glob.glob(os.path.join(dir_name, 'images', '*.png'))
        mask_files = glob.glob(os.path.join(dir_name, 'masks', '*.png'))

    print(f"No diretório {dir_name}:")
    print(f"Número de imagens: {len(img_files)}")
    print(f"Número de máscaras: {len(mask_files)}")

def replace_last_0000(s):
    return re.sub(r'(_0000)(?!.*_0000)', '', s)

def replace_last_000(s):
    return re.sub(r'(_000)(?!.*_000)', '', s)

def visualize_pairs(dir_name, n=5, is_overlay=False):
    if dir_name == cons.NNUNET_DIR: 
        img_files = glob.glob(os.path.join(dir_name, 'Dataset002_SacroRM', 'imagesTr', '*.png'))
        if not img_files:
            print(f"No images found in {dir_name}.")
            return
        shuffle(img_files)
        mask_files = [replace_last_000(img.replace('imagesTr', 'labelsTr')) for img in img_files]
    elif dir_name == cons.RESULT_DIR:
        img_files = glob.glob(os.path.join(dir_name, 'result001', 'imagesTs', '*.png'))
        if not img_files:
            print(f"No images found in {dir_name}.")
            return
        shuffle(img_files)
        mask_files = [replace_last_0000(img.replace('imagesTs', 'predicted')) for img in img_files]
    else:
        img_files = glob.glob(os.path.join(dir_name, 'images', '*.png'))
        shuffle(img_files)
        if not img_files:
            print(f"No images found in {dir_name}.")
            return
        mask_files = [img.replace('images', 'masks').replace('image_', 'mask_') for img in img_files]

    image_dataset = []
    mask_dataset = []

    for img, mask in zip(img_files, mask_files):
        img_arr = cv2.imread(img, cv2.IMREAD_GRAYSCALE)
        mask_arr = cv2.imread(mask, cv2.IMREAD_GRAYSCALE)

        image_dataset.append(img_arr)
        mask_dataset.append(mask_arr)

    image_dataset = np.array(image_dataset)
    mask_dataset = np.array(mask_dataset)

    print("Image name: ", img_files[0])
    print("Mask name: ", mask_files[0])
    print("Image type: ", type(image_dataset[0][0][0]))
    print("Mask type: ", type(mask_dataset[0][0][0]))
    print("Image directory: ", dir_name)
    print("Shape of image dataset: ", image_dataset.shape)
    print("Shape of mask dataset: ", mask_dataset.shape)
    print("Max pixel value in image is: ", image_dataset.max())
    print("Max pixel value in mask is: ", mask_dataset.max())
    print("Min pixel value in image is: ", image_dataset.min())
    print("Min pixel value in mask is: ", mask_dataset.min())
    print("Image dimensions are: ", image_dataset.shape[1], "x", image_dataset.shape[2])
    print("Labels in the mask are: ", np.unique(mask_dataset))
    print("Number of images: ", len(image_dataset))
    print("Number of masks: ", len(mask_dataset))
    print("Number of images with unique masks: ", len(np.unique(image_dataset, axis=0)))
    print("Number of masks with unique images: ", len(np.unique(mask_dataset, axis=0)))
    print()

    for i in range(min(n, len(image_dataset))):
        if not is_overlay:
            fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))
            ax1.imshow(image_dataset[i], cmap='gray')
            ax1.set_title('Image')
            ax2.imshow(mask_dataset[i], cmap='gray')
            ax2.set_title('Mask')
            plt.show()
        else:   
            fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))
            overlay = image_dataset[i].copy()
            overlay[mask_dataset[i] > 0] = 255  # Assuming mask values are binary (0 or 1)
            ax1.imshow(overlay, cmap='gray')
            ax1.set_title('Overlay')
            plt.show()


def check_channel_names():
    img = Image.open('nnUNet_raw/Dataset002_SacroRM/imagesTr/SRM_0447_0000.png')
    print(img.mode)  # Isso mostrará o número de canais e o tipo (por exemplo, "RGB" para imagens coloridas)
    print(img.size)  # 

## Checar modalidades dcm

import pydicom

def check_dcm_modality():
    dcm_file = pydicom.dcmread(cons.path_spair + 'teste.dcm')
    print("Modalidade:", dcm_file.Modality)


def convert_l_to_rgb_or_reverse(directory, type="L"):
    is_gray = True if type == "L" else False
    # Lista todos os arquivos do diretório
    for filename in os.listdir(directory):
        # Verifica se o arquivo é um PNG
        if filename.endswith(".png"):
            filepath = os.path.join(directory, filename)
            with Image.open(filepath) as img:
                if is_gray:
                    # Verifica se a imagem está no modo escala de cinza
                    if img.mode == "L":
                        # Converte para RGB
                        gray_img = img.convert("RGB")
                        # Salva a imagem convertida no mesmo local
                        gray_img.save(filepath)
                        print(f"Converted {filename} to RGB.")
                else:
                    # Verifica se a imagem está no modo RGB
                    if img.mode == "RGB":
                        # Converte para escala de cinza
                        rgb_img = img.convert("L")
                        # Salva a imagem convertida no mesmo local
                        rgb_img.save(filepath)
                        print(f"Converted {filename} to L.")




def overlay_with_bounding_box(dir_name, n=5, is_overlay=False):
    img_files = glob.glob(os.path.join(dir_name, 'result001', 'imagesTs', '*.png'))
    if not img_files:
        print(f"No images found in {dir_name}.")
        return
    shuffle(img_files)
    mask_files = [replace_last_0000(img.replace('imagesTs', 'predicted')) for img in img_files]
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


            # Display the image
            cv2.imshow("Image with Bounding Box", overlay)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

