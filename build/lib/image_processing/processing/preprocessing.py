from PIL import ImageFilter, ImageOps


def print_image(image):
    image.show()


def rotate_image(image, angle):
    return image.rotate(angle)


def detail_image(image):
    return image.filter(ImageFilter.DETAIL)


def cut_image(image, left, upper, right, lower):
    return image.crop((left, upper, right, lower))


def to_gray_scale(image):
    return ImageOps.grayscale(image)
