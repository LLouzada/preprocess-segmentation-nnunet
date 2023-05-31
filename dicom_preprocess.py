import glob
import cv2 as cv
import numpy as np
import pydicom as dicom
from PIL import Image
import shutil
import os

import variables as var


# Process the dicom images into png files
def dicomPreprocess(path):
    # Iterate through all dicom images in the directory
    for index, filename in enumerate(glob.iglob(path + '**/*.dcm', recursive=True)):
        img = dicom.dcmread(filename)
        center = img.WindowCenter
        width = img.WindowWidth
        slope = img.RescaleSlope
        intercept = img.RescaleIntercept
        rows = img.Rows
        columns = img.Columns
        output_img = Image.new('L', (columns, rows), 0)

        # Apply the windowing technique
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
        output_img.save(output_filename, 'png', compression="none")

    print("\nTotal: " + str(index+1) + " dicom images \n")

dicomPreprocess(var.path_spair)
        
