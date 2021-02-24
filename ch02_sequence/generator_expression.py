symbols = '$%#@#'
sym = tuple(ord(symbol) for  symbol in symbols)
print(sym)

import array
sym2 = array.array('I', (ord(symbol) for symbol in symbols))
print(sym2)


colors = ['black','white']
sizes = ['S', 'M', 'L']
for tshirt in ('%s %s'%(c,s) for c in colors for s in sizes):
    print(tshirt)