import collections

# StrKeyDict는 UserDict를 상속한다.
class StrKeyDict(collections.UserDict) :
# __missing__() 메서드는 Dict을 상속하는 예제와 완전히 똑같다.
    def __missing__(self, key):
        if isinstance(key,str) :
            raise KeyError(key)
        return self[str(key)]
# __contains__() 메서드는 더 간단하다.
# 저장된 키가 모두 str 형이므로 StrKeyDict0에서 self.keys()를 호출하는 방법과 달리
# self.data에서 바로 조회할 수 있다.
    def __contains__(self, key):
        return str(key) in self.data
# __setitem__() 메서드는 모든 키를 str 형으로 변환하므로, 
# 연산을 self.data에 위임할 때 더 간단히 작성할 수 있다.
    def __setitem__(self, key, item):
        self.data[str(key)] = item

d = StrKeyDict([('2','two'),('4','four')])
print(d['2'])
print(d['4'])
# print(d['1']) # KeyError: '1'
print(d.get('2'))
print(d.get('1','N/A'))