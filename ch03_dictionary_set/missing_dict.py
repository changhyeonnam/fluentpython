#StrKeyDict0이 dict 클래스를 상속한다.
class StrKeyDict0(dict) :
    def __missing__(self, key):
        # 키가 문자열인지 확인한다. 키가 문자열이고 존재하지 않으면 KeyError가 발생
        if isinstance(key,str):
            raise KeyError(key)
        # 키에서 문자열을 만들고 조회한다.
        return self[str(key)]

    def get(self, key, default=None):
        try :
            # get() 메서드는 self[key] 표기법을 이용해서 __getitem__() 메서드에 위임한다.
            # 이렇게 함으로써 __missing__()메서드가 작동할 기회를 준다.
            return self[key]
        except KeyError:
            # KeyError가 발생하면 __missinig__() 메서드가 이미 실패한 것이므로 default를 반환한다.
            return default

    def __contains__(self,key):
        # 수정하지 않은 (문자열이 아닐수 있는) 키를 검색하고 나서, 키에서 만든 문자열로 검색한다.
        return key in self.keys() or str(key) in self.keys()

d = StrKeyDict0([('2','two'),('4','four')])
print(d['2'])
print(d['4'])
print(d['1']) # KeyError: '1'
print(d.get('2'))
print(d.get('1','N/A'))