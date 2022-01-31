def caesar_cipher(string, offset):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    decoded = ""
    for char in string:
        position = alphabet.index(char)
        decode = alphabet[position - offset]
        decoded += decode
    return decoded
