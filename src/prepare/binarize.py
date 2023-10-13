# Caminho para a sua base de máscaras
import glob
import os
from PIL import Image
import cv2
import src.constants as cons

def binarize_masks():
    mask_directory = cons.AUGMENTED_DIR+'masks/'

    # List all masks in the directory
    mask_names = glob.glob(mask_directory + "*.png")

    for mask_path in mask_names:
        # Load the mask
        mask = cv2.imread(mask_path, 0)
        
        # Apply threshold
        _, binary_mask = cv2.threshold(mask, 127, 255, cv2.THRESH_BINARY)
        
        # Save the modified mask back to the directory
        cv2.imwrite(mask_path, binary_mask)


def convert_masks(input_path, output_path):
    # Listar todos os arquivos no diretório de entrada
    filenames = [f for f in os.listdir(input_path) if os.path.isfile(os.path.join(input_path, f))]
    
    for filename in filenames:
        # Abrir imagem usando PIL
        image = Image.open(os.path.join(input_path, filename))
        
        # Converter imagem para modo de escala de cinza (por precaução, caso não esteja)
        image = image.convert('L')
        
        # Converter [0, 255] para [0, 1]
        image = image.point(lambda p: p > 127 and 1)
        
        # Salvar imagem no diretório de saída
        image.save(os.path.join(output_path, filename))

