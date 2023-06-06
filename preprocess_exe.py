import argparse
from src.mask_preprocess import mask_preprocess
from src.dicom_preprocess import dicom_to_png
from src.check_result import check_sizes, check_pair
import src.constants as cons

# Cria o parser
parser = argparse.ArgumentParser(description='Preprocess the DICOM images and masks.')

# Adiciona os argumentos
parser.add_argument('--all', action='store_true', help='Preprocess everything')
parser.add_argument('--mask', choices=['all', 'spair', 'stir'], help='Preprocess masks, allowing to choose between SPair and STIR')
parser.add_argument('--dcmconvert', choices=['all', 'spair', 'stir'], help='Convert the DICOM images into PNG, allowing to choose between SPair and STIR')
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

# Se o argumento --all não foi fornecido, processa as máscaras se o argumento --mask foi fornecido
elif args.mask:
    print("\n ### Preprocessing masks ###################################### \n")
    if args.mask == 'all' or args.mask == 'spair':
        mask_preprocess(cons.path_spair)
    if args.mask == 'all' or args.mask == 'stir':
        mask_preprocess(cons.path_stir)

# Se o argumento --all não foi fornecido, converte as imagens DICOM em PNG se o argumento --dcm-convert foi fornecido
elif args.dcmconvert:
    print("\n ### Preprocessing DICOM images ################################## \n")
    if args.dcmconvert == 'all' or args.dcmconvert == 'spair':
        dicom_to_png(cons.path_spair)
    if args.dcmconvert == 'all' or args.dcmconvert == 'stir':
        dicom_to_png(cons.path_stir)

# Se o argumento --all não foi fornecido, verifica os tamanhos das imagens e máscaras se o argumento --check foi fornecido
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

# Se o argumento --all não foi fornecido, verifica os tamanhos das imagens e máscaras se o argumento --check foi fornecido
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

# Se o argumento --all não foi fornecido, verifica se há um par para cada imagem se o argumento --check foi fornecido
elif args.checkpair:
    print("\n ### Checking Pairs ################################## \n")
    if args.checkpair == 'all' or args.checkpair == 'spair-image':
        check_pair(cons.path_spair, "image")
    if args.checkpair == 'all' or args.checkpair == 'spair-mask':
        check_pair(cons.path_spair, "mask")
    if args.checkpair == 'all' or args.checkpair == 'stir-image':
        check_pair(cons.path_stir, "image")
    if args.checkpair == 'all' or args.checkpair == 'stir-mask':
        check_pair(cons.path_stir, "mask")
    




