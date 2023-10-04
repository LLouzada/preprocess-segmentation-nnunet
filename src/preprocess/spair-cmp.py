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

# PATH_DCM_FILES = "./SPAIR/"

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
# # Menores: 222 / Iguais: 77 / Maiores: 6

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
# # Menores: 222 / Iguais: 77 / Maiores: 6

# # Resize das imagens e mascaras

# PATH_DCM_FILES = "./SPAIR/"

# DIM_IMG_PADRAO = 384

# def resize_image(file):
#   img = Image.open(file)
#   px = img.load()
#   print("image name: " + str(file) + "\n" + str(img.size))
#   #img_array = np.array(img)
#   #display(img)
#   #print("size: " + str(img.size[0]))

#   if(img.size[0] != DIM_IMG_PADRAO):
#     #new_img = np.zeros((DIM_IMG_PADRAO,DIM_IMG_PADRAO), dtype = np.int8)
    
#     new_final = Image.new("L", (DIM_IMG_PADRAO,DIM_IMG_PADRAO))
#     for i in range(DIM_IMG_PADRAO):
#       for j in range(DIM_IMG_PADRAO):
#         new_final.putpixel([i,j], 0)

#     padding = int((DIM_IMG_PADRAO - img.size[0]) / 2)
#     x = img.size[0]
#     y = img.size[1]
#     for i in range(x):
#       for j in range(y):
#         if file[-3:] == "tif":
#           value_pixel = img.getpixel((i,j)) ## no caso se for uma imagem png sera do tipo ARGB no caso pegaremos apenas os 3 ultimos valores RGB
#           new_final.putpixel((i+padding, j+padding), value_pixel)
#         elif file[-3:] == "png" and type(img.getpixel((i,j))) is not int:
# #         print(f"TOTAL IMAGE PIXEL: {type(img.getpixel((i,j)))}")
#           value_pixel = img.getpixel((i,j))[1] ## no caso se for uma imagem png sera do tipo ARGB no caso pegaremos apenas os 3 ultimos valores RGB
# #         print(f"value_pixel: {value_pixel}\n")
#           new_final.putpixel((i+padding, j+padding), value_pixel)

#     #display(new_final)
#     #print("new image size: " + str(new_final.size[0]))
    
#     new_final.save(file, "PNG" ,compression="none") ### SALVAR A IMAGEM

# ################ Removemos o paciente com a imagem de dimensões maior que 384x384 #################
# ################################ paciente 35

# for index, filename in enumerate(glob.iglob(PATH_DCM_FILES + '**/*.tif', recursive=True)):
#   resize_image(filename)
#   print(f"index: {index}\n")

# for index, filename in enumerate(glob.iglob(PATH_DCM_FILES + '**/*.png', recursive=True)):
#   resize_image(filename)
#   print(f"index: {index}\n")

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
# # Menores: 0 / Iguais: 300 / Maiores: 0

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
# # Menores: 0 / Iguais: 299 / Maiores: 0