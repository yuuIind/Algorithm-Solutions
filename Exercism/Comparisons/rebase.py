def rebase(input_base, digits, output_base):
    if input_base < 2:
        raise ValueError("input base must be >= 2")
        
    if any(digit >= input_base for digit in digits):
        raise ValueError("all digits must satisfy 0 <= d < input base")
        
    if any(digit < 0 for digit in digits):
        raise ValueError("all digits must satisfy 0 <= d < input base")
    
    if output_base < 2:
        raise ValueError("output base must be >= 2")
    
    if input_base == output_base:
        return digits
    number = sum([digit*input_base**power for power, digit in enumerate(digits[::-1])])
    rebased_digits = []
    
    if number == 0:
        return [0]
