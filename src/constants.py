import os


# Ambiente
os.chdir('HCFMRP_sacroiliitis_v1')

path_spair = "./SPAIR/"
path_stir = "./STIR/"
TRAIN_DIR = './train/'
TEST_DIR = './test/'
AUGMENTED_DIR = './train/augmented/'
NNUNET_DIR = './nnUNet_raw/'
RESULT_DIR = './result/'
## Tamanho padrão das imagens
# Definido de acordo com os tamanhos das imagens do dataset (poucas imagens maiores são ignoradas)
default_image_size = 384