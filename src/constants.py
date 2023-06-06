import os


# Ambiente
os.chdir('HCFMRP_sacroiliitis_v1')

path_spair = "./SPAIR/"
path_stir = "./STIR/"

## Tamanho padrão das imagens
# Definido de acordo com os tamanhos das imagens do dataset (poucas imagens maiores são ignoradas)
default_size = 384