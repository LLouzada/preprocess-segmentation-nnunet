import glob
import cv2 as cv
import numpy as np
import pydicom as dicom
from PIL import Image
import shutil
import os
from tqdm import tqdm
import time

import src.variables as var


# Process the dicom images into png files
def dicomPreprocess(path):
    type = "SPAIR" if path == var.path_spair else "STIR"
    print("\n ### " + type)

    # Get all filenames into a list to iterate with tqdm
    all_files = list(glob.iglob(path + '**/*.dcm', recursive=True))
    
    start_time = time.time()

    processed_count = 0
    not_processed_count = 0

    # Iterate through all dicom images in the directory
    for index, filename in enumerate(tqdm(all_files, desc=f"Processing DICOM images",
                                          bar_format='{l_bar}{bar} [ elapsed time: {elapsed}, left: {remaining} ]')):
        img = dicom.dcmread(filename)
        try:
            center = img.WindowCenter
            width = img.WindowWidth
            slope = img.RescaleSlope
            intercept = img.RescaleIntercept
        except AttributeError:
            print(f"The file {filename} does not have one of the expected attributes. Skipping this file.")
            not_processed_count += 1
            continue
        rows = img.Rows
        columns = img.Columns
        output_img = Image.new('L', (columns, rows), 0)

        # Apply the windowing technique (https://radiopaedia.org/articles/windowing-ct)
        for i in range(rows):
            for j in range(columns):
                pixel = img.pixel_array[i][j] * slope + intercept
                if pixel <= center - 0.5 - (width - 1) / 2:
                    pixel = 0
                elif pixel > center - 0.5 + (width - 1) / 2:
                    pixel = 255
                else:
                    pixel = ((pixel - (center - 0.5)) / (width - 1) + 0.5) * 255 
                
                output_img.putpixel((j, i), int(pixel))

        output_filename = filename.replace('.dcm', '_processed.png')
        output_img.save(output_filename, 'png')

        processed_count += 1
        
    elapsed_time = time.time() - start_time

    print(f"\nTotal: {processed_count} ' + type + ' DICOM images processed")
    print(f"Not processed (atribute error): {not_processed_count} ' + type + ' DICOM images")
    print(f"Time elapsed: {elapsed_time} seconds")

        
