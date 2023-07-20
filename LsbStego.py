import numpy as np
from PIL import Image
def Encode(img, data):

    width, height = img.size
    array = np.array(list(img.getdata()))

    if img.mode == 'RGB':
        n = 3
    elif img.mode == 'RGBA':
        n = 4
    total_pixels = array.size//n

    data += "$$$$$"
    b_data = ''.join([format(ord(i), "08b") for i in data])
    required_pixels = len(b_data)

    if required_pixels > total_pixels:
        print("ERROR: Need larger file size")

    else:
        index=0
        for p in range(total_pixels):
            for q in range(0, n):
                if index < required_pixels:
                    array[p][q] = int(bin(array[p][q])[2:9] + b_data[index], 2)
                    index += 1

        array=array.reshape(height, width, n)
        encoded_image = Image.fromarray(array.astype('uint8'), img.mode)
        encoded_image.save("op.png")
        print("Image Encoded Successfully")
        return encoded_image



def Decode(img):

    array = np.array(list(img.getdata()))

    if img.mode == 'RGB':
        n = 3
    elif img.mode == 'RGBA':
        n = 4
    total_pixels = array.size//n

    hidden_bits = ""
    for p in range(total_pixels):
        for q in range(0, 3):
            hidden_bits += (bin(array[p][q])[2:][-1])

    hidden_bits = [hidden_bits[i:i+8] for i in range(0, len(hidden_bits), 8)]

    data = ""
    for i in range(len(hidden_bits)):
        if data[-5:] == "$$$$$":
            break
        else:
            data += chr(int(hidden_bits[i], 2))
    if "$$$$$" in data:
        print("Hidden data :", data[:-5])
    else:
        print("No Hidden data Found")
    return data[:-5]


