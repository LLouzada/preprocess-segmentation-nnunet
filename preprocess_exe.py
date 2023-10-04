import argparse
from src.preprocess.mask_preprocess import mask_preprocess
from src.preprocess.dicom_preprocess import dicom_to_png
from src.preprocess.check_result_preprocess import check_sizes, check_pair_unsplited, check_augmented_pair
from src.preprocess.resize import resize_stir, resize_spair
import src.constants as cons

# Cria o parser
parser = argparse.ArgumentParser(description='Preprocess the DICOM images and masks.')

# Adiciona os argumentos
parser.add_argument('--all', action='store_true', help='Preprocess everything')
parser.add_argument('--mask', choices=['all', 'spair', 'stir'], help='Preprocess masks, allowing to choose between SPair and STIR')
parser.add_argument('--dcmconvert', choices=['all', 'spair', 'stir'], help='Convert the DICOM images into PNG, allowing to choose between SPair and STIR')
parser.add_argument('--resize', choices=['all', 'spair', 'spair-masks', 'spair-images', 'stir', 'stir-masks', 'stir-images'], help='Resize the images and masks, allowing to choose between SPair and STIR, and between images and masks')
parser.add_argument('--checkresized', choices=['all', 'spair-masks', 'stir-masks', 'spair-images', 'stir-images'], help='Check the sizes of the resized images and masks, allowing to choose between SPair and STIR, and between images and masks') 
parser.add_argument('--checkunresized', choices=['all', 'spair-masks', 'stir-masks', 'spair-images', 'stir-images'], help='Check the sizes of the unresized images and masks, allowing to choose between SPair and STIR, and between images and masks')
parser.add_argument('--checkpair', choices=['all', 'spair-image', 'spair-mask', 'stir-image', 'stir-mask'], help= 'Check if there is a pair for each image and mask, allowing to choose between SPair and STIR, and between images and masks')

# Analisa os argumentos
args = parser.parse_args()

# Se o argumento --all foi fornecido, processe tudo
if args.all:
    print("\n ### Preprocessing masks ###################################### \n")
    mask_preprocess(cons.path_spair)
    mask_preprocess(cons.path_stir)
    print("\n ### Preprocessing DICOM images ################################## \n")
    dicom_to_png(cons.path_spair)
    dicom_to_png(cons.path_stir)
    #TODO: resize

# Processa as máscaras se o argumento --mask foi fornecido
elif args.mask:
    print("\n ### Preprocessing masks ###################################### \n")
    if args.mask == 'all' or args.mask == 'spair':
        mask_preprocess(cons.path_spair)
    if args.mask == 'all' or args.mask == 'stir':
        mask_preprocess(cons.path_stir)

# Converte as imagens DICOM em PNG se o argumento --dcm-convert foi fornecido
elif args.dcmconvert:
    print("\n ### Preprocessing DICOM images ################################## \n")
    if args.dcmconvert == 'all' or args.dcmconvert == 'spair':
        dicom_to_png(cons.path_spair)
    if args.dcmconvert == 'all' or args.dcmconvert == 'stir':
        dicom_to_png(cons.path_stir)

# Redimensiona as imagens e máscaras se o argumento --resize foi fornecido
elif args.resize:
    print("\n ### Resizing images and masks ################################## \n")
    if args.resize == 'all' or args.resize == 'spair':
        resize_spair("image")
        resize_spair("mask")
    if args.resize == 'all' or args.resize == 'stir':
        resize_stir("image")
        resize_stir("mask")
    if args.resize == "spair-masks":
        resize_spair("mask")
    if args.resize == "spair-images":
        resize_spair("image")
    if args.resize == "stir-masks":
        resize_stir("mask")
    if args.resize == "stir-images":
        resize_stir("image")

# Verifica os tamanhos das imagens e máscaras redimensionadas se o argumento --checkresized foi fornecido
elif args.checkresized:
    print("\n ### Checking sizes of the resized images and masks ################################## \n")
    if args.checkresized == 'all' or args.checkresized == 'spair-masks':
        check_sizes(cons.path_spair, "mask_resized")
    if args.checkresized == 'all' or args.checkresized == 'spair-images':
        check_sizes(cons.path_spair, "img_resized")  
    if args.checkresized == 'all' or args.checkresized == 'stir-masks':
        check_sizes(cons.path_stir, "mask_resized")
    if args.checkresized == 'all' or args.checkresized == 'stir-images':
        check_sizes(cons.path_stir, "img_resized")

# Verifica os tamanhos das imagens e máscaras antes de redimensionar se o argumento --checkunresized foi fornecido
elif args.checkunresized:
    print("\n ### Checking sizes of the unresized images and masks ################################## \n")
    if args.checkunresized == 'all' or args.checkunresized == 'spair-masks':
        check_sizes(cons.path_spair, "mask_unresized")
    if args.checkunresized == 'all' or args.checkunresized == 'spair-images':
        check_sizes(cons.path_spair, "img_unresized")
    if args.checkunresized == 'all' or args.checkunresized == 'stir-masks':
        check_sizes(cons.path_stir, "mask_unresized")
    if args.checkunresized == 'all' or args.checkunresized == 'stir-images':
        check_sizes(cons.path_stir, "img_unresized")

# Verifica se há um par para cada imagem se o argumento --checkpair foi fornecido
elif args.checkpair:
    print("\n ### Checking Pairs ################################## \n")
    if args.checkpair == 'all' or args.checkpair == 'spair-image':
        check_pair_unsplited(cons.path_spair, "image")
    if args.checkpair == 'all' or args.checkpair == 'spair-mask':
        check_pair_unsplited(cons.path_spair, "mask")
    if args.checkpair == 'all' or args.checkpair == 'stir-image':
        check_pair_unsplited(cons.path_stir, "image")
    if args.checkpair == 'all' or args.checkpair == 'stir-mask':
        check_pair_unsplited(cons.path_stir, "mask")





