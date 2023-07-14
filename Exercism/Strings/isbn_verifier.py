def is_valid(isbn):
    """
        - Given a string, the function checks if the provided string is a valid ISBN-10.
 
        - The program is able to verify ISBN-10 both with and without separating dashes.
    """
    # Remove dashes
    isbn = "".join(isbn.split("-"))
    
    # ISBN should have 10 digits
    if len(isbn) != 10:
        return False
        
    isbn_digits = []
    for index, digit in enumerate(isbn):
        # Handle Numeric digits
        if digit.isnumeric():
            isbn_digits.append(int(digit))
        # Handle the case of 'X' at the end of the ISBN    
        elif digit == 'X' and index==9:
            isbn_digits.append(10)
        # All the other cases for digits produce a not valid ISBN
        else:
            return False
            
    # Calculate the validity sum
    validity = sum(isbn_digits[i] * (10 - i) for i in range(10))
    return (validity % 11) == 0
