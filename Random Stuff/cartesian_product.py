# list comprehension
colours = ['black', 'white', 'blue', 'red']
sizes = ['S', 'M']
clothes = ['t-shirt', 'jeans', 'socks']

wardrobe = [(cl, colour, size) for cl in clothes
                                  for colour in colours
                                  for size in sizes]

print(wardrobe)

# generator expression
for item in (f'{cl} {c} {s}' for cl in clothes 
                              for c in colours 
                              for s in sizes):
    print(item)