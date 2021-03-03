# chapter03_dictionary and set (1)

Created: Mar 1, 2021 7:50 PM

dict 형은 애플리케이션에서 널리 사용될 뿐만아니라 파이썬 구현의 핵심부분이다. 

모듈 네임스페이스, 클래스 및 인스턴스 속성 함수의 키워드 인수 등 핵심 부분에 딕셔너리가 사용되고 있다. 내장 함수들은 __*builtins*__.__dict__에 들어 있다. 

중요한 역할을 맡고 있으므로 파이썬 dict 클래스는 상당히 최적화 되어 있다. 파이썬의 고성능 딕셔너리 뒤에는 해시테이블이라는 엔진이 있다. 

집합도 해시테이블을 이용해서 구현하므로, 이 장에서는 집합도 다룬다. 해시테이블이 작동하는 방식을 알아야 딕셔너리와 집합을 최대로 활용할 수 있다. 

이 장에서는 다음과 같은 내용을 설명한다.

- 공통적으로 사용되는 딕셔너리 메서드
- 없는 키에 대한 특별 처리
- 표준 라이브러리에서 제공하는 다양한 딕셔너리 클래스
- set과 frozenset 형
- 해시 테이블의 작동 방식
- 해시테이블의 의미 ( 키 자료형 제한, 예측할 수 없는 순서 등)

### 3.1 일반적인 매핑형

collenction.abc 모듈은 dict 및 이와 유사한 자료형의 인터페이스를 정의하기 위해 Mapping 및 MutableMapping 추상 베이스 클래스 (ABC)를 제공한다. 

표준 라이브러리에서 제공하는 매핑형은 모두 dict을 이용해서 구현해야 하므로, 키가 해시 가능해야한다는 제한을 갖고 있다. 

hashable(해시 가능하다) : 수명주기 동안 결코 변하지 않는 해시 값을 갖고 있고, (__hash__
() 메서드가 필요하다) 다른 객체와 비교할 수 있으며(__eq__() 메서드가 필요하다), 객체를 해시 가능하다고 한다. 동일하다고 판단되는 객체는 반드시 해시값이 동일해야 한다. immutable ( string, byte, int, float,...) frozenset 모두 해시 가능하다. 

```python
tt = (1,2,(30,40))
print(hash(tt))
t1 = (1,2,[30,40]) # hash 불가
print(hash(t1))
tf = (1,2,frozenset([30,40]))
print(hash(tf))
```

hash 값은 id()를 이용해서 구함. 객체가 자신의 내부 상태를 평가해서 __eq__() 메서드를 직접구현하는 경우에는 해시값 계싼에 사용되는 속성이 모두 불변형일 때만 해시 가능하다. 

```python
# dict을 구현하는 다양한 방법
a = dict(one=1,two=2,three=3)
b = {'one':1, 'two':2, 'three':3}
c = dict(zip(['one', 'two', 'three'], [1,2,3]))
d = dict([('two',2), ('one',1), ('three',3)])
e = dict({'three':3, 'one':1, 'two':2})
print(a == b == c == d == e)
```

### 3.2 dict comprehension

dict comprehension은 모든 반복형 객체에서 키- 값 쌍을 생성함으로써 딕셔너리 객체를 만들 수 있다. 

```python
DIAL_CODES = [
    (86,'china'),
    (91,'india'),
    (82,'korea'),
    (1,'USA'),
    (55,'Brazil')
]
country_code = {country: code for code, country in DIAL_CODES}
print(country_code)
```

### 3.3 공통적인 매핑 메서드

매핑이 제공하는 기본 API는 아주 많다. dict와 dict의 변형 중 가장 널리 사용되는 default와 OrderDict 클래스가 구현하는 메서드를 보여준다. 

- d.update(m, [**kargs])

    update() 메서드가 첫번째 인수를 다루는 방식은 dock typing의 대표적인 예이다. 먼저 m이 keys() 메서드를 갖고 있는지 확인한 후, 만약 메서드를 갖고 있으면 매핑이라고 간주한다. keys() 메서드가 없으면, update() 메서드는 m의 항목들이 (키,값) 쌍으로 되어 있다고 간주하고 m을 반복한다. 

- d. keys() : 키에 대한 뷰(?)를 가져 온다.
- d.setdefalut(k,[default]) : k in d가 참이면 d[k]를 반환하고, 아니면 d[k] = default로 설정하고 이 값을 반환한다.  이 메서드가 필요할 때는 똑같은 키를 여러번 조회하지 않게 해줌으로써 속도를 엄청나게 향상 시킨다.
- d.get(k,[default]) : k 키를 가진 항목을 반환한다. 해당 항목이 없다면 default나 None을 반환한다.

### 3.3.1 존재하지 않는 키를 setdefault()로 처리하기

fail-fast 철학에 따라, 존재하지 않는 킬 k로 d[k]에 접근하면 dict는 오류를 발생 시킨다. KeyError를 처리하는 것보다 기본값을 사용하는 것이 더 편리한 경우에는 d[k] 대신 d.get(k,default)를 사용한다는 것은 파이썬 개발자라면 누구나 알고 있다. 그렇지만 발견한 겂을 갱신할 때, 해당 객체가 가변 객체면 __**getitem**__() , __get__() 메서드는 보기 어색하며, 효율성도 떨어진다. 

```python
import sys
import re

WORD_RE = re.compile(r'\w+')
index = {}
with open(sys.argv[1], encoding='utf-8') as fp:
    for line_no, line in enumerate(fp,1):
        for match in WORD_RE.finditer(line):
            word = match.group()
            column_no = match.start() +1
            location = (line_no,column_no)
            '''
            word에 대한 occurences 리스트를 가져오거나, 단어가 없으면 빈 배열을 가져온다.
            새로 만든 location을 occurences에 추가한다.
            변경된 occurences를 index 딕셔너리에 넣는다. 그러면 index를 한번더 검사한다.
            '''
            occurences = index.get(word,[])
            occurences.append(location)
            index[word] = occurences

with open(sys.argv[1], encoding='utf-8') as fp:
    for line_no, line in enumerate(fp,1):
        for match in WORD_RE.finditer(line):
            word = match.group()
            column_no = match.start() +1
            location = (line_no,column_no)
            '''
            word에 대한 occurences 리스트를 가져오거나,word가 없을때는 빈 배열을 가져온다. 
            setdefault()가 값을 반환하므로 한번더 검색할 필요없이 갱신할 수 있다.
            '''
            index.setdefault(word,[]).append(location)

for word in sorted(index, key= str.upper):
    print(word, index[word])
```

### 3.4 융통성 있게 키를 조회하는 매핑

검색할 때 키가 존재하지 않으면 어떤 특별한 값을 반환하는 매핑이 있으면 편리한 때가 종종 있다. 이런 딕셔너리를 만드는 방법은 크게 두가지이다. 하나는 평범한 dict 대신 defaultdict를 사용하는 방법이고, 다른 하나는 dict 등의 매핑형을 상속해서 __missing__() 메서드를 추가하는 방법이다. 

### 3.4.1 defaultdict : 존재하지 않는 키에 대한 또 다른 처리

defaultdict는 존재하지 않는 키로 검색할 때 요청에 따라 항목을 생성하도록 되어 있다. 작동하는 방식은, defaultdict 객체를 생성할때 존재하지 않는 키 인수로 **getitem**() 메서드를 호출할때마다 기본 값을 생성하기 위해 사용되는 callable을 제공하는 것이다.

ex) dd = defaultdict(list) 코드로 기본 defultdict 객체를 생성한 후, dd에 존재하지 않는 키인 'new-key'로 dd['new-key'] 표현식을 실행하면 다음과 같이 처리된다. 

1. 리스트를 새로 생성하기 위해 list()를 호출한다.
2. new-key를 키로 사용해서 새로운 리스트를 dd에 삽입한다. 
3. 리스트에 대한 참조를 반환한다.

기본값을 생성하는 callable은 default_factory라는 객체 속성에 저장된다. 

default_factory가 설정되어 있지 않으면, 키가 없을 때 흔히 볼수 있는 keyError가 발생한다.

실제 defaultdict가 default_factory를 호출하게 만드는 메커니즘은 __missing__() 특수 메서드에 의존하며, 표준 매핑형은 모두 이 기능을 지원한다. 

### 3.4.2 __missing__() 메서드

__missing__() 메서드를 이용해서 존재하지 않는 키를 처리한다. 이 특수 메서드는 기본 클래스인 dict에는 정의되어 있지 않지만, dict은 이 메서드를 알고 있다. 따라서 dict 클래스를 상속하고 __missing__() 메서드를 정의하면, dict.__getitem__()  표준 메서드가 키를 발견할 수 없을 때 KeyError를 발생시키지 않고 __missing__() 메서드를 호출한다. 

```python
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
```

__missing__() 메서드에서 str(k) 키가 존재 하지 않으면 무한히 재귀적으로 호출된다. 그래서 isinstance(key,str) 코드가 필요하다. self[str(key)]가 str 키를 이용해서 __getitem__() 메서드를 호출하고, 이때 키가 없으면 __missing__() 메서드를 다시 호출하기 때문이다. 

### 3.5 그 외 매핑형

- collenctions.OrderedDict
- collections.ChainMap
- collections.Counter

```python
import collections

ct = collections.Counter('abracadabra')
print(ct)
ct.update('aaaazzzz')
print(ct)
print(ct.most_common(2))
```

OrderDict, ChainMap, Counter 클래스는 바로 사용할 수 있지만, UserDict는 다음 절에서 설명하는 것처럼 상속해서 사용하도록 설계되어 있다.

### 3.6 UserDict 상속하기

dict보다는 UserDict을 상속해서 매핑형을 만드는 것이 쉽다.  내장형에서는 아무런 문제없이 상속할 수 있는 메서드들을 오버라이드 해야 하는 구현의 특이성 때문에 dict 보다는 UserDict를 상속하는 것이 낫다.

UserDcit는 dict를 상속하지 않고 내부에 실제 항목을 담고 있는 data라고 하는 dict 객체를 갖고 있다. 이렇게 구현함으로써 __setitem__() 등의 특수 메서드를 구현할 때 발생하는 원치 않는 재귀적 호출을 피할 수 있으며, __cotains__() 메서드를 간단히 구현할 수 있다. 

UserDict 덕분에 StrKeyDict는 StrKeyDict0보다 간단하지만 더많은 일을 할 수 있도록 구현할 수 있다. StrKeyDict는 모든 key를 str 형으로 저장함으로써 비 문자열키로 객체를 생성하거나 갱신할 때 발생할 수 있는 예기치 못한 문제를 피하게 해준다. 

```python
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
```

UserDict 클래스가 MutableMapping을 상속하므로 StrKeyDict는 결국 UserDict, MutableMapping, 또는 Mapping을 상속하게 되어 매핑의 모든 기능을 가지게 된다. Mapping은 모든 추상 베이스 클래스(ABC)임에도 불구하고 유용한 concrete method를 다수 제공한다. 

- MutableMapping.updat()
- Mapping.get()

###