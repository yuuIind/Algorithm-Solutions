ACTIONS = ["wink",
           "double blink", 
           "close your eyes", 
           "jump", 
           "Reverse the order of the operations in the secret handshake."
          ]

def commands(binary_str):
    message = binary_str[-4:]
    code = []
    for index, action in enumerate(message[::-1]):
        if action == "1":
            code.append(ACTIONS[index])
    if binary_str[-5] == "1":
        code = code[::-1]    
    return code
