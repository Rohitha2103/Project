#RSA.py
import math
import cv2
import pywt
import random
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from huffman import HuffmanEncoding, HuffmanDecoding
from LsbStego import Encode,Decode

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", ",", ".", "!", "?", " "]
numbers = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31"]
def generate_keys():
    p=int(input("Enter prime number P: "))
    while not isPrime(p):
        print("%d is not a prime number!" % p)
        p = int(input("Please enter first prime number 'p' value again: "))
    q=int(input("Enter prime number q: "))
    while not isPrime(q):
        print("%d is not a prime number!" % q)
        q = int(input("Please enter second prime number 'q' value again: "))

    n=p*q
    print("n: ",n)
    e=int(input("e:"))
    while e <= 2 or gcd(phi(n),e) != 1:
        e=int(input("Invalid input, enter again: "))
    ph=phi(n)
    d = mod_inverse(e, ph)
    print("d: ",d)
    return n, d, e

def mod_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return -1

def isPrime(num):
    if num > 1:
        for i in range(2, num):
            if(num % i) == 0:
                return False
        else:
            return True
    else:
        return False
    
def gcd(a, b):
    while b != 0:
        (a, b) = (b, a % b)
    return a

def phi(n):
    amount = 0
    for k in range(1, n + 1):
        if math.gcd(n, k) == 1:
            amount += 1
    return amount

def cipher(num, e, n):
    X = []
    for i in range(len(num)):##1<num[i]<n
        if num[i]<=0 or num[i]>n:
            print("n value is small to encrypt data,")
            break
        X.append((num[i] ** e) % n)
    return X

def decipher(num, d, n):
    Y = []
    for i in range(len(num)):
        Y.append((num[i] ** d) % n)
    return Y

def Encrypt():    
    global text_encoded,img_encoded
    plaintext = input("Enter Plaintext: ").lower()
    numC = []
    numE=[]
    for i in range(len(plaintext)):
        for j in range(len(letters)):
            if(plaintext[i] == letters[j]):
                numC.append(int(numbers[j]))
                numE.append(letters[j])
    print(numC)            
    X = cipher(numC, e, n)
    print("Ciphertext:", X)
    print("Number of Ciphertext blocks:", len(X))
    text_encoded = HuffmanEncoding(X)
    if text_encoded:
        print("Compressed text:", text_encoded)
    original_image_file = (input("Enter image name (in png) :"))
    img = Image.open(original_image_file,'r')
    print(img, img.mode)
    encoded_image_file = "enc_" + original_image_file
    img_encoded = Encode(img, text_encoded)
    if img_encoded:
        img_encoded.save(encoded_image_file)
        print("{} saved!".format(encoded_image_file))
    original_image = Image.open(original_image_file)
    encoded_image = Image.open(encoded_image_file)
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))
    ax1.imshow(original_image)
    ax1.set_title('Original Image')
    ax2.imshow(encoded_image)
    ax2.set_title('Encoded Image')
    plt.show()
    return img_encoded


def Decrypt(img_encoded):
    encoded_image_file=input("Enter encoded image file: ")
    img2 = Image.open(encoded_image_file).convert('RGB')
    print(img2, img2.mode)
    hx=Decode(img2)
    hidden_text=[]
    hidden_text = HuffmanDecoding(hx)
    print("Decompressed text: ",hidden_text)
    Y = decipher(hidden_text, d, n)
    print("plaintext: ",Y)
    numD = []
    for i in range(len(Y)):
        for j in range(len(numbers)):
            if(Y[i] == int(numbers[j])):
                numD.append(letters[j])
 
    plaintext=" ".join(numD)
    print("Plain text: ",plaintext)
    for i in numD:
        print(i, end="")
    print("\n")
    return plaintext


text_encoded=""
img_encoded=""
def main():
    global n,d,e
    print("**** RSA encryption with Huffman coding and LSB steganography****")
    n,d,e=generate_keys()
    print("To encrypt a message with the current key, type 'Embedd'")
    print("To decrypt a message with the current key, type 'Extract'")
    print("To change values of keys,type 'change' ")
    print("Type 'quit' to exit")
    print('\n')
    print('\n')
    choice = str()
    choice = str()
    while choice != 'quit':
        choice = input("Enter Command: ")
        if choice.lower() == 'embedd':
            Encrypt()
        elif choice.lower() == 'extract':
            Decrypt(img_encoded)
        elif choice.lower() == 'change':
            n,e,d=generate_keys()

        elif choice.lower() == 'help':
                    print("To redefine n,e, or d, type 'n','e',... etc.")
                    print("To encrypt a message with the current key, type 'Embedd'")
                    print("To decrypt a message with the current key, type 'Extract'")
                    print("Type quit to exit")
                    print('\n')
                    print('\n')
        else:
            if choice != 'quit':
                ch = random.randint(0, 2)
                statements = ["This cannot be done","Just Type 'help' "]
                print(statements[ch])
if __name__ == "__main__":
    main()

