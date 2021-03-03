# my_dict = {}
# import collections.abc
# print(isinstance(my_dict,collections.abc.Mapping))

# tt = (1,2,(30,40))
# print(hash(tt))
# tf = (1,2,frozenset([30,40]))
# print(hash(tf))
# t1 = (1,2,[30,40])
# print(hash(t1))
#
# a = dict(one=1,two=2,three=3)
# b = {'one':1, 'two':2, 'three':3}
# c = dict(zip(['one', 'two', 'three'], [1,2,3]))
# d = dict([('two',2), ('one',1), ('three',3)])
# e = dict({'three':3, 'one':1, 'two':2})
# print(a == b == c == d == e)

DIAL_CODES = [
    (86,'china'),
    (91,'india'),
    (82,'korea'),
    (1,'USA'),
    (55,'Brazil')
]
country_code = {country: code for code, country in DIAL_CODES}
print(country_code)