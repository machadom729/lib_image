from PIL import Image


def open_image(path: str):
    return Image.open(path)


def save_image(imagem, path: str):
    imagem.save(path)
