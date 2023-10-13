import argparse
import os
import src.prepare.augmentator as aug
from src.prepare.split_data import split_data, organize_for_nnunet
from src.prepare.check_result_prepare import check_pairs, count_files, visualize_pairs, check_channel_names, check_dcm_modality, convert_l_to_rgb_or_reverse, overlay_with_bounding_box
from src.prepare.binarize import binarize_masks,  convert_masks
import src.constants as cons

# Cria o parser
parser = argparse.ArgumentParser(description='Prepare the data for training, splitting it into train and test sets and augmenting it.')

# Adiciona os argumentos
parser.add_argument('--split', choices=['all', 'spair', 'stir'], help='Split the data into train and test, allowing to choose between SPair and STIR')
parser.add_argument('--checkpairs', choices=['all', 'train', 'test', 'augmented', 'nnunet'], help='Check if the splits are correct')
parser.add_argument('--countfiles', choices=['all', 'train', 'test', 'augmented', 'nnunet'], help='Count the number of files in the splits')
parser.add_argument('--visualizepairs', choices=['all', 'train', 'test', 'augmented', 'nnunet', 'result'], help='Visualize the pairs in the splits, can change the number of pairs to visualize using --n argument')
parser.add_argument('--augment', action='store_true', help='Augment the images and masks (only train base)')
parser.add_argument('--n', type=int, default=2, help='Number of pairs to visualize')
parser.add_argument('--binarize', choices=['all', 'train', 'test', 'augmented'], help='Binarize the masks')
parser.add_argument('--organize', action='store_true', help='Organize the data for nnunet')
parser.add_argument('--test', action='store_true', help='Test')
parser.add_argument('--overlay', type=bool, default=False, help='Overlay the masks on the images when visualizing')
parser.add_argument('--convert', choices=['trainL', 'trainRGB', 'testL', 'testRGB', 'other'], help='Convert the images to RGB or L')

# Analisa os argumentos
args = parser.parse_args()

# Separa os dados em treino e teste se o argumento --split foi fornecido
if args.split:
    print("\n ### Splitting data ################################## \n")
    if args.split == 'all' or args.split == 'spair':
        split_data(cons.path_spair)
    if args.split == 'all' or args.split == 'stir':
        split_data(cons.path_stir)
    
# Checa se os pares estão corretos se o argumento --checkpairs foi fornecido
elif args.checkpairs:
    print("\n ### Checking pairs ################################## \n")
    if args.checkpairs == 'all' or args.checkpairs == 'train':
        check_pairs(cons.TRAIN_DIR)
    if args.checkpairs == 'all' or args.checkpairs == 'test':
        check_pairs(cons.TEST_DIR)
    if args.checkpairs == 'all' or args.checkpairs == 'augmented':
        check_pairs(cons.AUGMENTED_DIR)
    if args.checkpairs == 'all' or args.checkpairs == 'nnunet':
        check_pairs(cons.NNUNET_DIR)
    
# Conta o número de arquivos se o argumento --countfiles foi fornecido
elif args.countfiles:
    print("\n ### Counting files ################################## \n")
    if args.countfiles == 'all' or args.countfiles == 'train':
        count_files(cons.TRAIN_DIR)
    if args.countfiles == 'all' or args.countfiles == 'test':
        count_files(cons.TEST_DIR)
    if args.countfiles == 'all' or args.countfiles == 'augmented':
        count_files(cons.NNUNET_DIR)
    if args.countfiles == 'all' or args.countfiles == 'nnunet':
        count_files(cons.NNUNET_DIR)

# Visualiza os pares se o argumento --visualizepairs foi fornecido
elif args.visualizepairs:
    print("\n ### Visualizing pairs ################################## \n")
    if args.visualizepairs == 'all' or args.visualizepairs == 'train':
        visualize_pairs(cons.TRAIN_DIR, args.n, args.overlay)
    if args.visualizepairs == 'all' or args.visualizepairs == 'test':
        visualize_pairs(cons.TEST_DIR, args.n, args.overlay)
    if args.visualizepairs == 'all' or args.visualizepairs == 'augmented':
        visualize_pairs(cons.NNUNET_DIR, args.n, args.overlay)
    if args.visualizepairs == 'all' or args.visualizepairs == 'nnunet':
        visualize_pairs(cons.NNUNET_DIR, args.n, args.overlay)
    if args.visualizepairs == 'all' or args.visualizepairs == 'result':
        #visualize_pairs(cons.RESULT_DIR, args.n, args.overlay)
        overlay_with_bounding_box(cons.RESULT_DIR, args.n, args.overlay)

# Realiza o aumento de dados se o argumento --augment foi fornecido
elif args.augment:
    print("\n ### Augmenting data ################################## \n")
    #augment_data(args.n)
    aug.augment()

# Binariza as máscaras se o argumento --binarize foi fornecido
elif args.binarize:
    print("\n ### Binarizing masks ################################## \n")
    if args.binarize == 'all' or args.binarize == 'train':
        convert_masks(os.path.join(cons.TRAIN_DIR, 'masks'), os.path.join(cons.TRAIN_DIR, 'masks'))
    if args.binarize == 'all' or args.binarize == 'test':
        convert_masks(os.path.join(cons.TEST_DIR, 'masks'), os.path.join(cons.TEST_DIR, 'masks'))
    if args.binarize == 'all' or args.binarize == 'augmented':
        convert_masks(os.path.join(cons.AUGMENTED_DIR, 'masks'), os.path.join(cons.AUGMENTED_DIR, 'masks'))
    

# Organiza os dados para o nnunet se o argumento --organize foi fornecido
elif args.organize:
    print("\n ### Organizing data for nnunet ################################## \n")
    organize_for_nnunet()

# Testa se o argumento --test foi fornecido
elif args.test:
    print("\n ### Testing ################################## \n")
    check_channel_names()
    #check_dcm_modality()

# Converte as imagens se o argumento --convert foi fornecido
elif args.convert:
    if args.convert == 'trainL' or args.convert =='trainRGB':
        if args.convert == 'trainL':
            convert_l_to_rgb_or_reverse("nnUNet_raw/Dataset002_SacroRM/imagesTr/", 'L')
        else:
            convert_l_to_rgb_or_reverse("nnUNet_raw/Dataset002_SacroRM/imagesTr/", 'RGB')
    elif args.convert == 'testL' or args.convert =='testRGB':
        if args.convert == 'testL':
            convert_l_to_rgb_or_reverse("nnUNet_raw/Dataset002_SacroRM/imagesTs/", 'L')
        else:
            convert_l_to_rgb_or_reverse("nnUNet_raw/Dataset002_SacroRM/imagesTs/", 'RGB')
    elif args.convert == 'other':
            convert_l_to_rgb_or_reverse("test/images", 'RGB')

    
