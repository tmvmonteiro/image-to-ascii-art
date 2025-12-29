from functions import *
import sys
import os

input_location : str = "input/"
output_location : str = "output/"

small_alphabet = " -"
big_alphabet = ""

def main(file_name : str, scale : float | None = None, width : int | None = None, height : int | None = None) -> None:  
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
        ascii_matrix = pixel_colour_map(image_matrix, small_alphabet)
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
        

# The logic below needs to change to handle User Input correctly 
# P.E: <class 'NoneType'> : <class 'str'> : <class 'str'> shouldn't happen
if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("\nError: need to input file name (e.g.: tux.jpg) and scale or width/height")
        print("Usage: py -u main.py <file_name> <scale>")
        print("   or: py -u main.py <file_name> <width> <height>\n")
    else:
        if len(sys.argv) == 3:  # scale mode
            main(sys.argv[1], float(sys.argv[2]), None, None)
        elif len(sys.argv) == 4:  # width/height mode
            main(sys.argv[1], None, int(sys.argv[2]), int(sys.argv[3]))
        else:
            print("Error: too many arguments")