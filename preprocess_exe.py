from src.mask_preprocess import maskPreprocess
from src.dicom_preprocess import dicomPreprocess
import src.variables as var


print("\n ### Preprocessing masks ###################################### \n")
maskPreprocess(var.path_spair)
maskPreprocess(var.path_stir)

print("\n ### Preprocessing DICOM images ################################## \n")
dicomPreprocess(var.path_spair)
dicomPreprocess(var.path_stir)