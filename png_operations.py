def print_png_data(content):
    j = 0
    for i in range(len(content)):
        print(content[i], end=" ")
        j += 1
        if j == 16:
            j = 0
            print()


def image_width(content):
    image_width_hex = (str(content[16])[2:]) + (str(content[17])[2:]) + (str(content[18])[2:]) + (str(content[19])[2:])
    print('Image width:\t\t\t\t', end=" "), print(int(image_width_hex, 16))


def image_height(content):
    image_height_hex = (str(content[20])[2:]) + (str(content[21])[2:]) + (str(content[22])[2:]) + (str(content[23])[2:])
    print('Image height:\t\t\t\t', end=" "), print(int(image_height_hex, 16))


def image_bit_depth(content):
    image_bit_depth_hex = str(content[24])[2:]
    print('Image bit depth:\t\t\t', end=" "), print(int(image_bit_depth_hex, 16))


def image_colour_type(content):
    image_colour_type_hex = str(content[25])[2:]
    print('Image colour type:\t\t\t', end=" "), print(int(image_colour_type_hex, 16))


def image_compression_method(content):
    image_compression_method_hex = str(content[26])[2:]
    print('Image compression method:\t', end=" "), print(int(image_compression_method_hex, 16))


def image_filter_method(content):
    image_filter_method_hex = str(content[27])[2:]
    print('Image filter method:\t\t', end=" "), print(int(image_filter_method_hex, 16))


def image_interlace_method(content):
    image_interlace_method_hex = str(content[28])[2:]
    print('Image interlace method:\t\t', end=" "), print(int(image_interlace_method_hex, 16))


def show_ihdr_contents(content):
    print('Information from image header:')
    image_width(content)
    image_height(content)
    image_bit_depth(content)
    image_colour_type(content)
    image_compression_method(content)
    image_filter_method(content)
    image_interlace_method(content)
    print()


def print_ihdr_data(content, i):
    j = 0
    ihdr_length = content[i - 4][2:] + content[i - 3][2:] + content[i - 2][2:] + content[i - 1][2:]
    ihdr_length = int(ihdr_length, 16)
    print('IHDR chunk length: ', end=" "), print(ihdr_length, end=" "), print(' bytes')
    for a in range(ihdr_length + 4 + 4 + 4):  # metadata_length + 4 bytes length + 4 bytes name + 4 bytes CRC
        print(content[i - 4], end=" ")
        i += 1
        j += 1
        if j == 16:
            j = 0
            print()
    return ihdr_length


def print_idat_data(content, i):
    j = 0
    idat_length = content[i - 4][2:] + content[i - 3][2:] + content[i - 2][2:] + content[i - 1][2:]
    idat_length = int(idat_length, 16)
    print('IDAT chunk length: ', end=" "), print(idat_length, end=" "), print(' bytes')
    for a in range(idat_length + 4 + 4 + 4):  # metadata_length + 4 bytes length + 4 bytes name + 4 bytes CRC
        print(content[i-4], end=" ")
        i += 1
        j += 1
        if j == 16:
            j = 0
            print()
    return idat_length


def print_plte_data(content, i):
    j = 0
    plte_length = content[i - 4][2:] + content[i - 3][2:] + content[i - 2][2:] + content[i - 1][2:]
    plte_length = int(plte_length, 16)
    print('PLTE chunk length: ', end=" "), print(plte_length, end=" "), print(' bytes')
    for a in range(plte_length + 4 + 4 + 4):  # metadata_length + 4 bytes length + 4 bytes name + 4 bytes CRC
        print(content[i-4], end=" ")
        i += 1
        j += 1
        if j == 16:
            j = 0
            print()
    return plte_length


def print_iend_data(content, i):
    j = 0
    iend_length = content[i - 4][2:] + content[i - 3][2:] + content[i - 2][2:] + content[i - 1][2:]
    iend_length = int(iend_length, 16)
    print('IEND chunk length: ', end=" "), print(iend_length, end=" "), print(' bytes')
    for a in range(iend_length + 4 + 4 + 4):  # metadata_length + 4 bytes length + 4 bytes name + 4 bytes CRC
        print(content[i-4], end=" ")
        i += 1
        j += 1
        if j == 16:
            j = 0
            print()
    return iend_length
