def response(hey_bob):
    
    if hey_bob.isupper() and hey_bob.endswith('?'):
        return 'Calm down, I know what I\'m doing!'
    elif hey_bob.isupper():
        return 'Whoa, chill out!'
    elif hey_bob.strip().endswith('?'):
        return 'Sure.'
    elif hey_bob.isspace() or hey_bob == "":
        return 'Fine. Be that way!'
    else:
        return 'Whatever.'
