import glob
import cv2 as cv
import numpy as np
import pydicom as dicom
from PIL import Image
import shutil
from tqdm import tqdm
import time

import src.variables as var



# Process the segmentated images into masks
def maskPreprocess(path):
    type = "SPAIR" if path == var.path_spair else "STIR"
    print("\n ### " + type)
    
    # Get all filenames into a list to iterate with tqdm
    all_files = list(glob.iglob(path + '**/*.png', recursive=True))
    
    start_time = time.time()
    
    processed_count = 0

    # Iterate through all segmentated images in the directory (png files)
    for index, filename in enumerate(tqdm(all_files, desc=f"Processing {type} masks",
                                          bar_format='{l_bar}{bar} [ elapsed time: {elapsed}, left: {remaining} ]')):
        if not filename.endswith('_mask.png') and not filename.endswith('_processed.png'):

            # Read the image
            img = cv.imread(filename)
            img[img!=0] = 255

            # Remove noise using dilation and erosion
            kernel = np.ones((5,5),np.uint8)
            img = cv.dilate(img,kernel,iterations = 2)
            img = cv.erode(img,kernel,iterations = 2)

            # Save the image
            output_filename = filename.replace('.png', '_mask.png')
            cv.imwrite(output_filename, img)

            processed_count += 1
            
    elapsed_time = time.time() - start_time

    print("\nTotal: " + str(processed_count) + " " + type + " masks processed") 
    print(f"Time elapsed: {elapsed_time} seconds")





    


