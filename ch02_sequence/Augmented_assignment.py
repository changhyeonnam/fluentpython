# l = [1,2,3]
# print(l)
# print(id(l))
# l *= 2
# print(l)
# print(id(l))
#
# t = (1,2,3)
# print(id(t))
# print(t)
# t*=2
# print(id(t))
# print(t)

quiz
t = (1,2,[30,40])
t[2] += [50,60]
print(t)
# 지금은 안돌아 가네.. python 3.9, 3.5에서는 돌아갔다고 함.

import dis
print(dis.dis('s[a]+=b'))