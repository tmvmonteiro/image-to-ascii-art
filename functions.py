from PIL import Image, ImageFile
from io import TextIOWrapper

def initialize_image(file_name : str) -> ImageFile:
    return Image.open(file_name)    

def black_white(img : ImageFile) -> ImageFile:
    return img.convert("L")

def image_resize(img : ImageFile, width : int, height : int) -> ImageFile:
    return img.resize((width, height))

def image_rescale(img : ImageFile, scale : float) -> ImageFile:
    new_width : int = round(img.width * scale)
    new_height : int = round(img.height * scale)
    return img.resize((new_width, new_height))

def pixel_matrix_parse(img : ImageFile) -> list:
    matrix = []
    for y in range(img.height):
        row = []
        for x in range(img.width):
            pixel : int = img.getpixel((x, y))
            row.append(pixel)
        matrix.append(row)
    return matrix

def pixel_colour_map(image_matrix : list, alphabet : str) -> list:
    ascii_matrix = []
    threshold = 256 // len(alphabet)
    for image_row in image_matrix:
        ascii_row = []
        for image_pixel in image_row:
            alphabet_value: int = image_pixel // threshold
            ascii_pixel : str = alphabet[alphabet_value]
            ascii_row.append(ascii_pixel)
        ascii_matrix.append(ascii_row)
    return ascii_matrix

def create_file(matrix : list, output_file : TextIOWrapper) -> None:
    for row in matrix:
        line : str = ""
        for char in row:
            line += char
        line += '\n'
        output_file.write(line)