l = ['spam','spam','eggs','spam']
print(set(l))
print(list(set(l)))

# dis.dis() 디어셈블러 함수
from dis import dis
print(dis('{1}'))
print(dis('set([1])'))
print(frozenset(range(10)))

from unicodedata import name
code = {chr(i) for i in range(32,256) if 'SIGN' in name(chr(i),'')}
print(code)