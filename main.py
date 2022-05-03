# import numpy as np
# import sys
import binascii
from PIL import Image
import png_operations as png

IHDR_hex = '0x490x480x440x52'
PLTE_hex = '0x500x4c0x540x45'
IDAT_hex = '0x490x440x410x54'
IEND_hex = '0x490x450x4e0x44'

tEXt_hex = '0x740x450x580x74'
tIME_hex = '0x740x490x4d0x45'
gAMA_hex = '0x670x410x4d0x41'
cHRM_hex = '0x630x480x520x4d'


image = Image.open('.\\PNG_images\\icon.png')
image.show()

file_path = '.\\PNG_images\\icon.png'

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
    if (str(content[i]) + str(content[i + 1]) + str(content[i + 2]) + str(content[i + 3])) == IDAT_hex:
        print()
        idat_length = png.print_idat_data(content, i)
        idat_start.append(i - 4)
        idat_end.append(idat_start[x] + 4 + 4 + idat_length + 4)
        critical_chunks_space += (idat_end[x] - idat_start[x])
        tmp += png.save_critical_chunk_to_tmp(content, idat_start[x], idat_end[x])
        print()
        x += 1
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
        gama = content[i + 4][2:] + content[i + 5][2:] + content[i + 6][2:] + content[i + 7][2:]
        gama = int(gama, 16)
        gama = gama/100000
        print("Gamma value: ", end=" "), print(gama)
        print()
    if (str(content[i]) + str(content[i + 1]) + str(content[i + 2]) + str(content[i + 3])) == cHRM_hex:
        print()
        cHRM_start = i - 4
        cHRM_length = png.print_chrm_data(content, i)
        cHRM_end = cHRM_start + 4 + 4 + cHRM_length + 4
        print()

file.close()
# print(), print(critical_chunks_space)
# print()
# print()
# print(image_info)
# print(tmp)

tmp = image_info + tmp
tmp = tmp.strip()
tmp = tmp.replace(' ', '')
tmp = tmp.replace('\n', '')
tmp = binascii.a2b_hex(tmp)
with open('.\\PNG_images\\icon-po-anonimizacji.png', 'wb') as file2:
    file2.write(tmp)

file2.close()

# png_operations.print_png_data(content)

# a = np.fft.fft2([[1, 2], [3, 4]])
# print()
# print(a)
# print(np.fft.fftshift(a))
# print(np.abs(a))
