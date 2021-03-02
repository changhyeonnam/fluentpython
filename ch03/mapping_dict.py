import collections

ct = collections.Counter('abracadabra')
print(ct)
ct.update('aaaazzzz')
print(ct)
print(ct.most_common(2))