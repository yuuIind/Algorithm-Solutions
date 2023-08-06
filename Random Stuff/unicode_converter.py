symbols = 'ığüşöç'
codes = []

for symbol in symbols:
    codes.append(ord(symbol))

print(codes)


# list comprehension

codes = [ord(symbol) for symbol in symbols]
print(codes)