from functions import *
import os
import argparse

input_location : str = "input/"
output_location : str = "output/"

def main(file_name : str, alphabet : str, scale : float | None = None, width : int | None = None, height : int | None = None) -> None:  
    try:
        img = initialize_image(str(input_location+file_name))
    except Exception as e:
        print(f"Error: Couldn't open Image : {e}")
        return
    try:
        black_white_img = black_white(img) 
    except Exception as e:
        print(f"Error: Couldn't convert Image to Grayscale : {e}")
        return
    try:
        if scale is None and (width is not None and height is not None):
            black_white_img = image_resize(black_white_img, width, height)
        elif scale is not None and (width is None and height is None):
            black_white_img = image_rescale(black_white_img, scale)
    except Exception as e:
        print(f"Error: Couldn't resize/rescale Image : {e}")
        return
    try:
        image_matrix = pixel_matrix_parse(black_white_img)
    except Exception as e:
        print(f"Error: Couldn't parse Image Pixels values into the Matrix : {e}")
        return 
    try:
        ascii_matrix = pixel_colour_map(image_matrix, alphabet)
    except Exception as e:
        print(f"Error: Couldn't map the Matrix values into ASCII Characters : {e}")
        return
    try:
        base_name = os.path.splitext(file_name)[0]
        txt_file_name = base_name + '.txt'
        output_file : TextIOWrapper = open(str(output_location+txt_file_name), "w")
        create_file(ascii_matrix, output_file)
        output_file.close()
    except Exception as e:
        print(f"Error: Couldn't create/write content into Output File : {e}")
        return
        
if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("file_name", type=str)

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--scale", type=float)
    group.add_argument("--width", type=int)

    parser.add_argument("--height", type=int)
    parser.add_argument("--alphabet", type=str, default=" -")

    args = parser.parse_args()

    file_name = args.file_name
    alphabet = args.alphabet

    if args.scale is not None:
        scale = args.scale
        width = None
        height = None
    else:
        scale = None
        width = args.width
        height = args.height

    main(file_name, alphabet, scale, width, height)