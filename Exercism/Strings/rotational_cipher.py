import string

def rotate(text, key):

    """
    - Implementation of the rotational cipher, also sometimes called the Caesar cipher.
    - The Caesar cipher is a simple shift cipher that relies on transposing all the letters in the
    alphabet using an integer key between 0 and 26. 
    - The letter is shifted for as many values as the value of the key.
    - The general notation for rotational ciphers is ROT + <key>. 

    Parameters
    ----------
    text : str
        text to be ciphered.
    key : int
        key value to be used for ciphering.

    Returns
    -------
    str
        The ciphered version of ``text`` according to ``key``.
    
    Examples
    --------
    >>> rotate("omg", 5)
    "trl"
    
    """
    ALPHABET = string.ascii_lowercase
    cipher = ALPHABET[key:] + ALPHABET[:key]
    encrypter = str.maketrans(ALPHABET+ALPHABET.upper(), cipher+cipher.upper())
    return text.translate(encrypter)
