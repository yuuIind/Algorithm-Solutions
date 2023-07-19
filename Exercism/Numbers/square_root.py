def square_root(number):
    eps = 0.0001 
    guess = number / 2 + eps
    error = eps*10
    while error > eps:
        a = (number - guess**2) / (2 * guess)
        b = guess + a
        guess = b - (a**2 / (2*b))
        error = abs(number - guess*guess)
    return int(guess)
