from PIL import Image, ImageEnhance

def aumentar_brilho(imagem_path, fator):
    # Abre a imagem
    img = Image.open(imagem_path)
    
    # Verifica se a imagem está no mode "L"
    if img.mode != 'L':
        raise ValueError("A imagem não está no mode 'L'. Converta-a para escala de cinza primeiro.")

    enhancer = ImageEnhance.Brightness(img)
    img_bright = enhancer.enhance(fator)

    img_bright.show()

    img_bright.save(imagem_path.replace('_052_', '_115_'))

