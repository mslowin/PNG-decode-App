import numpy as np
# import sys
import binascii
import png_operations as png
import matplotlib.pyplot as plt
from PIL import Image
from skimage.io import imread, imshow
from skimage.color import rgb2hsv, rgb2gray, rgb2yuv
from skimage import color, exposure, transform
from skimage.exposure import equalize_hist

IHDR_hex = '0x490x480x440x52'
PLTE_hex = '0x500x4c0x540x45'
IDAT_hex = '0x490x440x410x54'
IEND_hex = '0x490x450x4e0x44'

tEXt_hex = '0x740x450x580x74'
tIME_hex = '0x740x490x4d0x45'
gAMA_hex = '0x670x410x4d0x41'
cHRM_hex = '0x630x480x520x4d'
pHYs_hex = '0x700x480x590x73'


image = Image.open('.\\PNG_images\\easyPNG.png')
# image.show()

file_path = '.\\PNG_images\\easyPNG.png'

with open(file_path, 'rb') as file:
    content = [hex(a) for a in file.read()]


# png.print_png_data(content)


i = 0
x = 0
flag = 0
idat_start = []
idat_end = []
critical_chunks_space = 0
tmp = ''

text_length = 'brak tekstu'
image_info = png.extract_image_info(content)

for i in range(len(content)-3):
    # print((str(content[i]) + str(content[i + 1]) + str(content[i + 2]) + str(content[i + 3])))
    if (str(content[i]) + str(content[i + 1]) + str(content[i + 2]) + str(content[i + 3])) == IHDR_hex:
        print()
        png.show_ihdr_contents(content)
        ihdr_length = png.print_ihdr_data(content, i)
        ihdr_start = 8
        ihdr_end = ihdr_start + 4 + 4 + ihdr_length + 4
        critical_chunks_space += (ihdr_end - ihdr_start)
        tmp = png.save_critical_chunk_to_tmp(content, ihdr_start, ihdr_end)
        print()
    if (str(content[i]) + str(content[i + 1]) + str(content[i + 2]) + str(content[i + 3])) == PLTE_hex:
        print()
        plte_length = png.print_plte_data(content, i)
        plte_start = i - 4
        plte_end = plte_start + 4 + 4 + plte_length + 4
        critical_chunks_space += (plte_end - plte_start)
        tmp += png.save_critical_chunk_to_tmp(content, plte_start, plte_end)
        print()
    # if (str(content[i]) + str(content[i + 1]) + str(content[i + 2]) + str(content[i + 3])) == IDAT_hex:
    #     print()
    #     idat_length = png.print_idat_data(content, i)
    #     idat_start.append(i - 4)
    #     idat_end.append(idat_start[x] + 4 + 4 + idat_length + 4)
    #     critical_chunks_space += (idat_end[x] - idat_start[x])
    #     tmp += png.save_critical_chunk_to_tmp(content, idat_start[x], idat_end[x])
    #     print()
    #     x += 1
    if (str(content[i]) + str(content[i + 1]) + str(content[i + 2]) + str(content[i + 3])) == IEND_hex:
        print()
        iend_length = png.print_iend_data(content, i)
        iend_start = i - 4
        iend_end = iend_start + 4 + 4 + iend_length + 4
        critical_chunks_space += (iend_end - iend_start)
        tmp += png.save_critical_chunk_to_tmp(content, iend_start, iend_end)
        print()
    # # ancillary chunks:
    if (str(content[i]) + str(content[i + 1]) + str(content[i + 2]) + str(content[i + 3])) == tEXt_hex:
        print()
        text_length = png.print_text_data(content, i)
        text_start = i - 4
        text_end = text_start + 4 + 4 + text_length + 4
        print()
    if (str(content[i]) + str(content[i + 1]) + str(content[i + 2]) + str(content[i + 3])) == tIME_hex:
        print()
        time_length = png.print_time_data(content, i)
        time_start = i - 4
        time_end = time_start + 4 + 4 + time_length + 4
        print()
    if (str(content[i]) + str(content[i + 1]) + str(content[i + 2]) + str(content[i + 3])) == gAMA_hex:
        print()
        gama_start = i - 4
        gama_length = png.print_gama_data(content, i)
        gama_end = gama_start + 4 + 4 + gama_length + 4
        print()
    if (str(content[i]) + str(content[i + 1]) + str(content[i + 2]) + str(content[i + 3])) == cHRM_hex:
        print()
        cHRM_start = i - 4
        cHRM_length = png.print_chrm_data(content, i)
        cHRM_end = cHRM_start + 4 + 4 + cHRM_length + 4
        print()
    if (str(content[i]) + str(content[i + 1]) + str(content[i + 2]) + str(content[i + 3])) == pHYs_hex:
        print()
        pHYS_start = i - 4
        pHYs_length = png.print_phys_data(content, i)
        pHys_end = pHYS_start + 4 + 4 + pHYs_length + 4
        print()

file.close()
# print(), print(critical_chunks_space)
# print()
# print()
# print(image_info)
# print(tmp)


# putting together whole PNG file data, (first 8 bytes of png file which are always the same + the rest of the file):
tmp = image_info + tmp
tmp = tmp.strip()
tmp = tmp.replace(' ', '')   # getting rid of all unnecessary spaces and end of lines
tmp = tmp.replace('\n', '')
tmp = binascii.a2b_hex(tmp)  # changing hex data to binascii
with open('.\\PNG_images\\icon-po-anonimizacji.png', 'wb') as file2:
    file2.write(tmp)

file2.close()

# png_operations.print_png_data(content)

image2 = imread('.\\PNG_images\\ball.png')

plt.figure()
plt.imshow(image2, cmap='gray')

image2_fourier = np.fft.fftshift(np.fft.fft2(image2))
out = np.log(abs(image2_fourier))

plt.figure()
plt.imshow(out, cmap='gray')
plt.show()
