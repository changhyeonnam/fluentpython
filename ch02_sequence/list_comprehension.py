symbols = '$%#@#'
codes = []
for symbol in symbols:
    codes.append(ord(symbol))
print(codes)

codes2 = []
codes2 = [ord(symbol) for symbol in symbols]
print(codes2)

x = 'ABC'
dummy = [ord(x) for x in x]
print(x)
print(dummy)

symbols = '$%#@#'
beyond_ascii = [ord(s) for s in symbols if ord(s) > 30]
print(beyond_ascii)

beyond_ascii = list(filter(lambda c:c>30,map(ord,symbols)))
print(beyond_ascii)