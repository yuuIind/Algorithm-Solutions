def is_isogram(string):
    """
        - Determines if a word or phrase is an isogram.
 
        - An isogram (also known as a "non-pattern word") is a word or phrase without a repeating
        letter, however spaces and hyphens are allowed to appear multiple times.
 
        - Examples of isograms:
            - lumberjacks
            - background
            - downstream
            - six-year-old
    """
    marked = [] # letters that has seen in the string previously
    string = string.lower()
    for letter in string:
        if letter in marked and letter.isalpha():
            return False
        else: 
            marked.append(letter)
    return True
