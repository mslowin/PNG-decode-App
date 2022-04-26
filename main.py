# import numpy as np
# import sys
from PIL import Image
import png_operations as png

IHDR_hex = '0x490x480x440x52'
PLTE_hex = '0x500x4c0x540x45'
IDAT_hex = '0x490x440x410x54'
IEND_hex = '0x490x450x4e0x44'


image = Image.open('.\\PNG_images\\icon.png')
image.show()

file_path = '.\\PNG_images\\icon.png'
# file_path = '..\\png-is-my-favourite-file-type-master\\png_files\\type_3.png'

with open(file_path, 'rb') as file:
    content = [hex(a) for a in file.read()]

# png.print_png_data(content)


i = 0
x = 0

idat_start = []
idat_end = []

for i in range(len(content)-3):
    # print((str(content[i]) + str(content[i + 1]) + str(content[i + 2]) + str(content[i + 3])))
    if (str(content[i]) + str(content[i + 1]) + str(content[i + 2]) + str(content[i + 3])) == IHDR_hex:
        print()
        png.show_ihdr_contents(content)
        ihdr_length = png.print_ihdr_data(content, i)
        ihdr_start = 8
        ihdr_end = ihdr_start + 4 + 4 + ihdr_length + 4
        print()
    if (str(content[i]) + str(content[i + 1]) + str(content[i + 2]) + str(content[i + 3])) == PLTE_hex:
        print()
        plte_length = png.print_plte_data(content, i)
        plte_start = i - 4
        plte_end = plte_start + 3 + 4 + plte_length + 4
        print()
    if (str(content[i]) + str(content[i + 1]) + str(content[i + 2]) + str(content[i + 3])) == IDAT_hex:
        print()
        idat_length = png.print_idat_data(content, i)
        idat_start.append(i - 4)
        idat_end.append(idat_start[x] + 3 + 4 + idat_length + 4)
        print()
        x += 1
    if (str(content[i]) + str(content[i + 1]) + str(content[i + 2]) + str(content[i + 3])) == IEND_hex:
        print()
        iend_length = png.print_iend_data(content, i)
        iend_start = i - 4
        iend_end = iend_start + 3 + 4 + iend_length + 4
        print()


# png_operations.print_png_data(content)

# a = np.fft.fft2([[1, 2], [3, 4]])
# print()
# print(a)
# print(np.fft.fftshift(a))
# print(np.abs(a))
