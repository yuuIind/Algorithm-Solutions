def is_pangram(sentence):
    """
        - Figures out if a sentence is a pangram.
 
        - A pangram is a sentence using every letter of the alphabet at least once. 
        
        - It is case insensitive, so it doesn't matter if a letter is lower-case (e.g. k) or upper-case
    (e.g. K).
    
        - Only checks the basic letters used in the English alphabet: a to z.
    """
    ALPHABET = 'abcdefghijklmnopqrstuvwxyz' # alphabet
    sentence = sentence.lower() # ensure case insensitivity
    return set(ALPHABET).issubset(set(sentence))
