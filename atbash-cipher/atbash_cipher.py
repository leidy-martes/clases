import string
import re


ENCODE = str.maketrans(
    string.ascii_letters,
    ''.join(reversed(string.ascii_lowercase + string.ascii_lowercase)),
    string.punctuation + string.whitespace)

DECODE = str.maketrans(
    string.ascii_lowercase,
    ''.join(reversed(string.ascii_lowercase)),
    string.whitespace)


def encode(plain_text):
    nueva_palabra = plain_text.translate(ENCODE)
    recortado = re.findall(r'.{1,5}', nueva_palabra)
    return ' '.join(recortado)


def decode(ciphered_text):
    return ciphered_text.translate(DECODE)
