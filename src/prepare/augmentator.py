# import glob
# import os
# import time
# import albumentations as A
# import cv2
# from tqdm import tqdm
# import src.constants as cons# v2

# import os
# from PIL import Image
# import numpy as np
# import albumentations as A

# def load_and_transform_image(image_path, transform):
#     image = Image.open(image_path)
#     image_np = np.array(image)
#     transformed_image_np = transform(image=image_np)['image']
#     return Image.fromarray(transformed_image_np)

# def save_transformed_images(directory, transform):
#     # Lista todas as imagens no diretório com o padrão de nome especificado
#     images = [img for img in os.listdir(directory) if img.startswith("SRM_") and img.endswith(".png")]

#     # Encontra o último número do nome das imagens originais
#     if images:
#         latest_number = max(int(img.split('_')[1]) for img in images)
#     else:
#         latest_number = 0

#     # Percorre todas as imagens e aplica a transformação duas vezes
#     for image_name in images:
#         image_path = os.path.join(directory, image_name)
        
#         # Aplica a transformação na imagem original e salva
#         for i in range(2):
#             latest_number += 1
#             transformed_image = load_and_transform_image(image_path, transform)
#             new_image_name = f"SRM_{latest_number:03}_0000.png"
#             transformed_image.save(os.path.join(directory, new_image_name))

# # Definindo a transformação
# height, width = cons.default_image_size, cons.default_image_size
# transform = A.Compose([
#     A.HorizontalFlip(p=0.5),
#     A.VerticalFlip(p=0.5),
#     A.Rotate(limit=30, p=0.5),
#     A.RandomSizedCrop(min_max_height=(int(0.8*height), height), height=height, width=width, p=0.5),
#     A.GridDistortion(p=0.4),
#     A.GaussNoise(p=0.4),
# ])





# import src.constants as cons

# height = cons.default_image_size
# width = cons.default_image_size

# #TODO adicionar os imagens originais (sem aumentação) na base final

# # Define the transformations
# transform = A.Compose([
#     A.HorizontalFlip(p=0.5),
#     A.VerticalFlip(p=0.5),
#     A.Rotate(limit=30, p=0.5),
#     A.RandomSizedCrop(min_max_height=(int(0.8*height), height), height=height, width=width, p=0.5)
# ])

# def augment_data(n):
#     path = os.path.join(cons.NNUNET_DIR, 'Dataset002_SacroRM', 'imagesTr')  # Adjusted to point directly to the images directory

#     # Create directory to save augmented data if doesn't exist
#     augmented_dir = os.path.join(cons.TRAIN_DIR, 'augmented')
#     os.makedirs(os.path.join(augmented_dir, 'images'), exist_ok=True)
#     os.makedirs(os.path.join(augmented_dir, 'masks'), exist_ok=True)

#     # Get all image filenames into a list to iterate with tqdm
#     image_files = list(glob.iglob(path + '/*.png', recursive=True))

#     start_time = time.time()
#     processed_count = 0

#     # Iterate through all image files
#     for image_path in tqdm(image_files, desc="Processing images", bar_format='{l_bar}{bar} [ elapsed time: {elapsed}, left: {remaining} ]'):
#         # Get the corresponding mask path
#         mask_path = image_path.replace("images", "masks").replace("image", "mask")

#         # Load the image and mask
#         image = cv2.imread(image_path)
#         mask = cv2.imread(mask_path, cv2.IMREAD_GRAYSCALE)

#         if image is None or mask is None:
#             print(f"Failed to load image or mask. Image: {image_path}, Mask: {mask_path}")
#             continue

#         # Save original image and mask to the augmented directory with "_og" suffix
#         original_image_path = os.path.join(augmented_dir, 'images', os.path.basename(image_path).replace('.png', '_og.png'))
#         original_mask_path = os.path.join(augmented_dir, 'masks', os.path.basename(mask_path).replace('.png', '_og.png'))

#         cv2.imwrite(original_image_path, image)
#         cv2.imwrite(original_mask_path, mask)

#         # Apply the transformation n times
#         for i in range(n):
#             transformed = transform(image=image, mask=mask)

#             transformed_image = transformed["image"]
#             transformed_mask = transformed["mask"]

#             # Construct paths for augmented images and masks
#             transformed_image_path = os.path.join(augmented_dir, 'images', os.path.basename(image_path).replace('.png', f'_aug_{i}.png'))
#             transformed_mask_path = os.path.join(augmented_dir, 'masks', os.path.basename(mask_path).replace('.png', f'_aug_{i}.png'))

#             cv2.imwrite(transformed_image_path, transformed_image)
#             cv2.imwrite(transformed_mask_path, transformed_mask)

#             processed_count += 1
        
#     elapsed_time = time.time() - start_time
#     elapsed_time = time.strftime("%H:%M:%S", time.gmtime(elapsed_time))

#     print("\nTotal: " + str(processed_count) + " images augmented")
#     print(f"Time elapsed: {elapsed_time} seconds")



# #TODO FIX
#     # Caminho para a sua base de máscaras
# mask_directory = '/path_to_your_mask_directory/'

# # Liste todas as máscaras no diretório
# mask_names = glob.glob(mask_directory + "*.png")

# for mask_path in mask_names:
#     # Carregue a máscara
#     mask = cv2.imread(mask_path, 0)
    
#     # Aplique threshold
#     _, binary_mask = cv2.threshold(mask, 127, 255, cv2.THRESH_BINARY)
    
#     # Normalize (embora isso seja opcional, pois o valor já estará em 0 ou 255)
#     binary_mask = binary_mask / 255.0
    
#     # Converta de volta para uint8 para salvar como PNG
#     binary_mask = (binary_mask * 255).astype('uint8')
    
#     # Salve a máscara modificada de volta ao diretório
#     cv2.imwrite(mask_path, binary_mask)

#     ## USE

#     #TODO remove below
# # Realiza o aumento de dados se o argumento --augment foi fornecido
# # elif args.augment:
# #     print("\n ### Augmenting data ################################## \n")
# #     if args.augment == 'all' or args.augment == 'spair':
# #         augment_data(cons.path_spair)
# #     if args.augment == 'all' or args.augment == 'stir':
# #         augment_data(cons.path_stir)

# # # Verifica se há um par para cada imagem aumentada se o argumento --checkaugmentedpair foi fornecido
# # elif args.checkaugmentedpair:
# #     print("\n ### Checking Pairs ################################## \n")
# #     if args.checkaugmentedpair == 'all' or args.checkaugmentedpair == 'spair-image':
# #         check_augmented_pair(cons.path_spair, "image")
# #     if args.checkaugmentedpair == 'all' or args.checkaugmentedpair == 'spair-mask':
# #         check_augmented_pair(cons.path_spair, "mask")
# #     if args.checkaugmentedpair == 'all' or args.checkaugmentedpair == 'stir-image':
# #         check_augmented_pair(cons.path_stir, "image")
# #     if args.checkaugmentedpair == 'all' or args.checkaugmentedpair == 'stir-mask':
# #         check_augmented_pair(cons.path_stir, "mask")
# # #TODO remove below
# # def check_augmented_pair(path, type):
# #     type1 = "_processed_resized_flipped.png" if type == "image" else "_mask_resized_flipped.png"
# #     type2 = "_mask_resized_flipped.png" if type == "image" else "_processed_resized_flipped.png"
# #     path_type = "SPAIR" if path == cons.path_spair else "STIR"

# #     all_files = list(glob.iglob(path + "**/*" + type1, recursive=True))
# #     all_files2 = list(glob.iglob(path + "**/*" + type2, recursive=True))

# #     pair = 0
# #     no_pair = 0
# #     no_pair_list = []

# #     for index, filename in enumerate(all_files):
# #         if filename.endswith(type1):
# #             if filename.replace(type1, type2) in all_files2:
# #                 pair += 1
# #             else:
# #                 no_pair += 1
# #                 print(filename + " has no pair")
# #                 no_pair_list.append(filename)

# #     print(f"\n{type.capitalize()} {path_type} - Pair check")
# #     print(f" - Pair: {pair}")
# #     print(f" - No pair: {no_pair}\n")
# #     # print(no_pair_list)

# # parser.add_argument('--augment', choices=['all', 'spair', 'stir'], help='Augment the images and masks, allowing to choose between SPair and STIR')
# # parser.add_argument('--checkaugmentedpair', choices=['all', 'spair-image', 'spair-mask', 'stir-image', 'stir-mask'], help= 'Check if there is a pair for each image and mask, allowing to choose between SPair and STIR, and between images and masks')
import os
import cv2
import albumentations as A
import src.constants as cons

# Defina a transformação
height, width = cons.default_image_size, cons.default_image_size

transform = A.Compose([
    A.HorizontalFlip(p=0.5),
    A.VerticalFlip(p=0.5),
    A.Rotate(limit=30, p=0.5),
    A.RandomSizedCrop(min_max_height=(int(0.8*height), height), height=height, width=width, p=0.5),
    A.GridDistortion(p=0.4),
    A.GaussNoise(p=0.4),
])

image_dir = os.path.join(cons.NNUNET_DIR, 'Dataset002_SacroRM', 'imagesTr')
label_dir = os.path.join(cons.NNUNET_DIR, 'Dataset002_SacroRM', 'labelsTr')

def augment():
    # Lista os arquivos nas pastas de imagens e mascaras
    images = [f for f in os.listdir(image_dir) if f.endswith('.png')]
    labels = [f for f in os.listdir(label_dir) if f.endswith('.png')]

    # Definindo o índice inicial para as novas imagens e máscaras (de acordo com o ultimo index das images)
    index = max([int(f.split('_')[1]) for f in images]) + 1

    for image_file, label_file in zip(images, labels):
        # Ler a imagem e a mascara
        image = cv2.imread(os.path.join(image_dir, image_file))
        mask = cv2.imread(os.path.join(label_dir, label_file), 0)

        # Aplica a transformação 2 vezes
        for i in range(2):
            augmented = transform(image=image, mask=mask)
            image_transformed = augmented['image']
            mask_transformed = augmented['mask']

            # Salve a imagem e a mascara transformadas
            new_image_name = f"SRM_{index:04}_0000.png"
            new_label_name = f"SRM_{index:04}.png"

            cv2.imwrite(os.path.join(image_dir, new_image_name), image_transformed)
            cv2.imwrite(os.path.join(label_dir, new_label_name), mask_transformed)

            # Incrementando o índice
            index += 1
