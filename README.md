# Project
*RSA Encryption with Huffman Coding and LSB Steganography*

**Description**


This project implements RSA encryption, Huffman coding, and Least Significant Bit (LSB) steganography techniques. 
It allows users to encrypt and decrypt messages using RSA encryption, compress the encrypted text using Huffman coding and hide the compressed text within images using LSB steganography.

**Features**



●  RSA encryption with key generation


●  Huffman coding for text compression


●  LSB steganography for hiding compressed text in images

**
Requirements && Prerequisites **

●  Python 3.x

Libraries:

    ● cv2
    
    ● pywt
    
    ● numpy
    
    ● matplotlib
    
    ● PIL (Python Imaging Library)
   
**   Usage:**

1. Run the RSA.py file, The script will prompt you to generate RSA keys (p, q, n, e, and d) or use the existing keys.

2. Choose the "Embedd" option to encrypt a plaintext message. Enter the message when prompted.

3. The script will convert the plaintext to a numeric representation, encrypt it using RSA, compress it using Huffman coding, and then hide it within an image using LSB steganography.

4. The encoded image will be saved as enc_original_image_name.png.

5. Choose the "Extract" option to decrypt the hidden message from an encoded image. Provide the name of the encoded image (e.g., enc_image.png) when prompted.

6. The script will extract the compressed text from the image, decompress it using Huffman decoding, and then decrypt it using RSA to retrieve the original plaintext.
    
