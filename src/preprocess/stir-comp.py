# # Converte

# def process_dicom_to_tif_file(file):
#   image = dicom.dcmread(file)
#   center = image.WindowCenter
#   width = image.WindowWidth
#   rescaleSlope = image.RescaleSlope
#   rescaleIntercept = image.RescaleIntercept
#   rows = image.Rows
#   columns = image.Columns
#   img_final = Image.new("L", (columns,rows))
#   for i in range(rows):
#     for j in range(columns):
#       value_n = image.pixel_array[i,j] * rescaleSlope + rescaleIntercept
            
#       if value_n <= center - 0.5  - (width-1) / 2:
#         value_n = 0
#       elif value_n > center - 0.5  + (width-1) / 2:
#         value_n = 255
#       else:
#         value_n = ((value_n - (center - 0.5)) / (width-1) + 0.5) * 255
            
#       img_final.putpixel([j,i], int(value_n))
  
#   img_final.save(os.path.join(file.split(".dcm")[0] + ".tif"), "TIFF", compression="none")
#   #cv_imshow(img_final.show)

# ###########################################################################
# ############ GERANDO OS .tif para todas as imagens de um paciente #########
# ###########################################################################

# PATH_DCM_FILES = "./STIR/"

# for index, filename in enumerate(glob.iglob(PATH_DCM_FILES + '**/*.dcm', recursive=True)):
#   process_dicom_to_tif_file(filename)
#   print(filename)


# # Checa tamanho e quantidade das imagens convertidas

# men = 0
# igu = 0
# mai = 0
# for index, filename in enumerate(glob.iglob(PATH_DCM_FILES + '**/*.tif', recursive=True)):
#   img = Image.open(filename)
#   larg, alt = img.size
  
  
#   if(int(larg) < 384):
#     men = men + 1
#   elif(int(larg) == 384):
#     igu = igu + 1
#   elif(int(larg) > 384):
#     mai = mai + 1

# print("Quantidade de imagens (384x384)\n\nMenores: "  + str(men) + " / Iguais: "  + str(igu) + " / Maiores: "  + str(mai))

# # Quantidade de imagens (384x384)
# # Menores: 0 / Iguais: 0 / Maiores: 270

# # Checa tamanho e quantidade das mascaras

# men = 0
# igu = 0
# mai = 0
# for index, filename in enumerate(glob.iglob(PATH_DCM_FILES + '**/*.png', recursive=True)):
#   img = Image.open(filename)
#   larg, alt = img.size
  
  
#   if(int(larg) < 384):
#     men = men + 1
#   elif(int(larg) == 384):
#     igu = igu + 1
#   elif(int(larg) > 384):
#     mai = mai + 1

# print("Quantidade de imagens (384x384)\n\nMenores: "  + str(men) + " / Iguais: "  + str(igu) + " / Maiores: "  + str(mai))

# # Quantidade de imagens (384x384)
# # Menores: 0 / Iguais: 0 / Maiores: 270

# # Resize das mascaras

# DIM_IMG_PADRAO = 384

# # Resize máscaras

# for index, filename in enumerate(glob.iglob(PATH + '**/*.png', recursive=True)):
#   print("\n IMAGEM: " + filename)
#   print("\n INDEX: " + str(index))

#   img = cv.imread(filename)
#   res = cv.resize(img, dsize = (DIM_IMG_PADRAO, DIM_IMG_PADRAO), interpolation=cv.INTER_AREA)
#   cv.imwrite(filename, res)
  
# # Resize das imagens

#   DIM_IMG_PADRAO = 384

# # Resize imagens

# for index, filename in enumerate(glob.iglob(PATH + '**/*.tif', recursive=True)):
#   print("\n IMAGEM: " + filename)
#   print("\n INDEX: " + str(index))

#   img = cv.imread(filename)
#   res = cv.resize(img, dsize = (DIM_IMG_PADRAO, DIM_IMG_PADRAO), interpolation=cv.INTER_AREA)
#   cv.imwrite(filename, res)

# # Checa tamanho e quantidade das imagens depois do resize

# men = 0
# igu = 0
# mai = 0
# for index, filename in enumerate(glob.iglob(PATH_DCM_FILES + '**/*.tif', recursive=True)):
#   img = Image.open(filename)
#   larg, alt = img.size
  
  
#   if(int(larg) < 384):
#     men = men + 1
#   elif(int(larg) == 384):
#     igu = igu + 1
#   elif(int(larg) > 384):
#     mai = mai + 1

# print("Quantidade de imagens (384x384)\n\nMenores: "  + str(men) + " / Iguais: "  + str(igu) + " / Maiores: "  + str(mai))

# # Quantidade de imagens (384x384)
# # Menores: 0 / Iguais: 270 / Maiores: 0

# # Checa tamanho e quantidade das mascaras depois do resize

# men = 0
# igu = 0
# mai = 0
# for index, filename in enumerate(glob.iglob(PATH_DCM_FILES + '**/*.png', recursive=True)):
#   img = Image.open(filename)
#   larg, alt = img.size
  
  
#   if(int(larg) < 384):
#     men = men + 1
#   elif(int(larg) == 384):
#     igu = igu + 1
#   elif(int(larg) > 384):
#     mai = mai + 1

# print("Quantidade de imagens (384x384)\n\nMenores: "  + str(men) + " / Iguais: "  + str(igu) + " / Maiores: "  + str(mai))

# # Quantidade de imagens (384x384)
# # Menores: 0 / Iguais: 270 / Maiores: 0