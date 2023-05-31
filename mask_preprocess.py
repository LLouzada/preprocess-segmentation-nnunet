import glob
import cv2 as cv
import numpy as np
import pydicom as dicom
from PIL import Image
import shutil

import variables as var



# Process the segmentated images into masks
def maskPreprocess(path):
    type = "SPAIR" if path == var.path_spair else "STIR"
    print("\n" + type)

    # Iterate through all segmentated images in the directory (png files)
    for index, filename in enumerate(glob.iglob(path + '**/*.png', recursive=True)):
        if not filename.endswith('_mask.png') and not filename.endswith('_processed.png'):
            print("\n file name: " + filename)
            print("index: " + str(index))

            # Convert all non-black pixels to white
            img = cv.imread(filename)
            img[img!=0] = 255

            # View the images (uncomment to view)
            # cv.imshow('image', img)
            # cv.waitKey(0)

            # Remove noise using dilation and erosion
            kernel = np.ones((5,5),np.uint8)
            img = cv.dilate(img,kernel,iterations = 2)
            img = cv.erode(img,kernel,iterations = 2)

            # View the images (uncomment to view)
            # cv.imshow('image', img)
            # cv.waitKey(0)

            # Save the image
            output_filename = filename.replace('.png', '_mask.png')
            cv.imwrite(output_filename, img)


    print("\nTotal: " + str(index+1) + " " + type + " images \n")



    


