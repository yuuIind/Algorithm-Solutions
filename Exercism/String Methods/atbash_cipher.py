import string
PLAIN = string.ascii_lowercase
CIPHER = PLAIN[::-1]
def encode(plain_text):
    ciphered_text = ""
    for c in plain_text.lower():
        if c.isdigit():
            ciphered_text += c
        elif c.isalpha():
            cipher = CIPHER[PLAIN.find(c)]
            ciphered_text += cipher
    groups = [ciphered_text[index:index+5] for index in range(0, len(ciphered_text), 5)]
    return " ".join(groups)


def decode(ciphered_text):
    plain_text = ""
    for c in ciphered_text.lower():
        if c.isdigit():
            plain_text += c
        elif c.isalpha():
            cipher = PLAIN[CIPHER.find(c)]
            plain_text += cipher
    return plain_text
