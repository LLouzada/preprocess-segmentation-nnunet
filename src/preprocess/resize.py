import glob
from PIL import Image
import cv2 as cv
from tqdm import tqdm
import time
import src.constants as cons


def resize_stir(type):
    path = cons.path_stir
    print("\n ### STIR resize")

    resize_type = "_processed.png" if type == "image" else "_mask.png"

    # Get all filenames into a list to iterate with tqdm
    all_files = list(glob.iglob(path + '**/*' + resize_type, recursive=True))

    start_time = time.time()

    processed_count = 0

    # Iterate through all files
    for index, filename in enumerate(tqdm(all_files, desc=f"Resizing STIR {type}s",
                                            bar_format='{l_bar}{bar} [ elapsed time: {elapsed}, left: {remaining} ]')):
        # Read the image
        img = cv.imread(filename)

        # Resize the image
        img = cv.resize(img, (cons.default_size, cons.default_size), interpolation=cv.INTER_AREA)

        # Save the image
        output_filename = filename.replace(resize_type, resize_type.replace(".png", "_resized.png"))
        cv.imwrite(output_filename, img)

        processed_count += 1

    elapsed_time = time.time() - start_time
    # convert seconds to hours, minutes and seconds
    elapsed_time = time.strftime("%H:%M:%S", time.gmtime(elapsed_time))

    print("\nTotal: " + str(processed_count) + " STIR " + type + "s resized")
    print(f"Time elapsed: {elapsed_time} seconds")

def resize_spair(rtype):
    path = cons.path_spair
    print("\n ### SPAIR resize")

    resize_type = "_processed.png" if rtype == "image" else "_mask.png"

    # Get all filenames into a list to iterate with tqdm
    all_files = list(glob.iglob(path + '**/*' + resize_type, recursive=True))

    start_time = time.time()

    processed_count = 0

    # Iterate through all files
    for index, filename in enumerate(tqdm(all_files, desc=f"Resizing SPAIR {rtype}s",
                                            bar_format='{l_bar}{bar} [ elapsed time: {elapsed}, left: {remaining} ]')):
        # Read the image
        img = Image.open(filename)
        # print("image name: " + str(filename) + "\n" + str(img.size))

        if img.size[0] > cons.default_size or img.size[1] > cons.default_size:
            continue  # Pular a iteração se a imagem for maior do que a dimensão padrão

        if(img.size < (cons.default_size, cons.default_size)):
            output = Image.new("L", (cons.default_size, cons.default_size))
            for i in range(cons.default_size):
                for j in range(cons.default_size):
                    output.putpixel((i, j), 0)
        
        padding = int((cons.default_size - img.size[0]) / 2)
        x = img.size[0]
        y = img.size[1]

        for i in range(x):
            for j in range(y):
                if(type(img.getpixel((i,j))) is not int):
                    output.putpixel((i + padding, j + padding), img.getpixel((i, j))[1])
                else:
                    output.putpixel((i + padding, j + padding), img.getpixel((i, j)))
                    
        
        # Save the image
        output_filename = filename.replace(resize_type, resize_type.replace(".png", "_resized.png"))
        output.save(output_filename)

        processed_count += 1

    elapsed_time = time.time() - start_time
    # convert seconds to hours, minutes and seconds
    elapsed_time = time.strftime("%H:%M:%S", time.gmtime(elapsed_time))

    print("\nTotal: " + str(processed_count) + " SPAIR " + rtype + "s resized")
    print(f"Time elapsed: {elapsed_time} seconds")







