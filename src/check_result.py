import glob
from PIL import Image

import src.constants as cons

def check_sizes(path, type):
    enum_type = ""
    print_type = ""
    path_type = "SPAIR" if path == cons.path_spair else "STIR"
    match type:
        case "mask_unresized":
            enum_type = "**/*_mask.png"
            print_type = "Unresized masks"
        case"img_unresized":
            enum_type = "**/*_processed.png"
            print_type = "Unresized images"
        case "mask_resized":
            enum_type = "**/*_mask_resized.png"
            print_type = "Resized masks"
        case "img_resized":
            enum_type = "**/*_processed_resized.png"
            print_type = "Resized images"

    smaller = 0
    bigger = 0
    same = 0

    for index, filename in enumerate(glob.iglob(path + enum_type, recursive=True)):
        img = Image.open(filename)
        widht, height = img.size
  
  
        if(int(widht) < 384):
            smaller += 1
        elif(int(widht) == 384):
            same += 1
        elif(int(widht) > 384):
            bigger += 1
    
    print(f"\n{print_type} {path_type} - defaut size: {cons.default_size} x {cons.default_size}")
    print(f" - Smaller: {smaller}")
    print(f" - Bigger: {bigger}")
    print(f" - Same: {same} \n")

def check_pair(path, type):
    type1 = "_processed.png" if type == "image" else "_mask.png"
    type2 = "_mask.png" if type == "image" else "_processed.png"
    path_type = "SPAIR" if path == cons.path_spair else "STIR"

    all_files = list(glob.iglob(path + "**/*" + type1, recursive=True))
    all_files2 = list(glob.iglob(path + "**/*" + type2, recursive=True))

    pair = 0
    no_pair = 0
    no_pair_list = []

    for index, filename in enumerate(all_files):
        if filename.endswith(type1):
            if filename.replace(type1, type2) in all_files2:
                pair += 1
            else:
                no_pair += 1
                print(filename + " has no pair")
                no_pair_list.append(filename)

    print(f"\n{type.capitalize()} {path_type} - Pair check")
    print(f" - Pair: {pair}")
    print(f" - No pair: {no_pair}\n")
    # print(no_pair_list)

    