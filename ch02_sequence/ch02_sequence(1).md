# chapter02_sequence(1)

Created: Feb 23, 2021 6:55 PM

파이썬은 시퀀스를 단일하게 처리하는 ABC의 특징을 물려받음. 문자열, 리스트, 바이트 시퀀스, 배열, XML 요소, 데이터베이스 결과에는 모두 반복, 슬라이싱, 정렬,  연결  등 공통된 연산 적용 가능. 

파이썬에서 제공하는 다양한 시퀀스를  이해하면 코드를 새로 구현할 필요가 없으며, 시퀀스의 공통 인터페이스를 따라 기존 혹은 향후에 구현될 시퀀스 자료형을  적절히 지원하고 활용할 수 있게 API를 정의할 수 있다. 파이썬 3에서 새로 소개된 바이트 자료형까지 주로 시퀀스에 해당하는 내용을 설명한다. 리스트, 튜플, 배열, 큐에 대해서도 구체적으로 설명하지만 유니코드 문자열에 대해서는 4장에서 다룬다. 표준 라이브러리에서 제공하는 시퀀스를 사용하며 시퀀스형을 구현하는 방법은 10장에서 설명한다. 

### 2.1 내장 시퀀스 개요

파이썬 표준 라이브러리 C로 구현된 다음과 같은 시퀀스형을 제공한다. 

- 컨테이너 시퀀스 (container sequence) : 서로 다른 자료형의 항목들을 담을 수 있는 list, tuple, collections, deque 형. 객체에 대한 참조를 담고 있으며, 객체는 어떠한 자료형도 될수 있다.
- 균일 시퀀스 (flat sequence) : 단 하나의 자료형 만을 담을 수 있는 str, bytes, btyearray, memoryview, array.array 형. 객체에 대한 참조 대신 자신의 메모리 공간에 각 항목의 값을 직접 담는다.

→ flat sequence가 메모리를 더  적게 사용하지만, 문자, 바이트, 숫자  등 기본적인 자료형만 저장할 수 있다. 

시퀀스 형은 다음과 같이 가변성에 따라 분류할 수 도 있다.

- 가변 시퀀스 (mutable sequence): list, bytearray,  array.array, collections.deque, memoryview 형
- 불변 시퀀스 (immutable sequence) : tuple, str, bytes 형

가변과 불변 그리고 컨테이너와 균일에 대한 이런 일반적인 성질을 기억해 두면 앞으로 나올 구체적인 시퀀스형의 기능을 가늠하는데 도움을 준다. 

가장 기본적인 시퀀스형인 list는 가변적이며 혼합된 자료형을 담을 수 있다. list comprehension을 잘 알고 있으면 generator experssion도 쉽게 이해할 수 있다. 

### 2.2 list comprehension과 generator expression

### 2.2.1 list comprehension과 가독성

```python
symbols = '$%#@#'
codes = []
for symbol in symbols:
    codes.append(ord(symbol))
print(codes)

codes2 = []
codes2 = [ord(symbol) for symbol in symbols]
print(codes2)
```

list  comprehension이 두줄이상 넘어가는 경우에는 코드를 분할하거나 for문을 이용해서 작성하는 것이 낫다. 

**지능형 리스트는  더이상 메모리를 누수하지 않는다**

python 2.x 같은 경우 메모리 누수의 문제 발생했었슴.

list comprehension, generator expression 그리고 이와 동급인 set comprehension과 dict comprehension는 함수 처럼 고유한 지역 범위를 갖는다. 표현식 안에서 할당된 변수는 지역 변수지만, 주변 범위의 변수를 여전히 참조할 수 있다. 

```python
x = 'ABC'
dummy = [ord(x) for x in x]
print(x)
print(dummy)
```

1. x의 값이 유지 된다.
2. list comprehension이 기대했던 리스트를 만든다. 

list comprehension는 항목을 filtering 및 mapping함 으로써 시퀀스나 기타 iterable 자료형으로부터 리스트를 만든다. 다음 절에서 설명하는 것처럼 내장된 filter()와  map() 함수를 사용해서 동일한 작업을 수행할  수 있지만 가독성은 떨어진다. 

### 2.2.2 list comprehension과 map() / filter() 비교

map() 과 fileter() 함수를 이용해서 수행할 수 있는 작업은 기능적으로 문제가 있는 파이썬 lambda를 억지로 끼워 넣지 않고도 list comprehension을 이용해서 모두 구현할 수 있다. 

```python
symbols = '$%#@#'
beyond_ascii = [ord(s) for s in symbols if ord(s) > 30]
print(beyond_ascii)

beyond_ascii = list(filter(lambda c:c>30,map(ord,symbols)))
print(beyond_ascii)
```

### 2.2.3 데카르트 곱

list comprehension는 두개 이상의 iterable 자료형의 데카르트 곱을 나타내는 일련의 리스트를 만들 수 있다. 데카르트 곱 안에 들어 있는 각 항목은 입력으로 받은 iterable data의 각 요소에서 만들어진 tuple로 구성된다. 

생성된 리스트의 길이는 입력으로 받은 반복 가능한 데이터의 길이와 동일하다.

예를들어 두가지 색상과 세가지 크기의 티셔츠 리스트를 만드는 경우를 생각해보자. 여섯개의 항목이 만들어 진다.

```python
colors = ['black', 'white']
sizes = ['S','M','L']
tshirts = [(color,size) for color in colors for size in sizes]
print(tshirts)

for  color in colors :
    for size in sizes :
        print((color, size))

tshirts = [(color,size)  for  size in sizes for color in colors]
print(tshirts)

'''
1. color 다음에 size를 배치해서 만든 튜플 리스트를 생성한다.
2. color를 반복하는 루프안에서 sizes를 반복해서 튜플 리스트를 출력한다.
3. 먼저 size를 반복하고 그 안에서 color로 반복하려면 for문의 순서만 바꾸면 된다.
'''
```

13가지 순위와 4가지 종류로 구성된 52장의 카드 한 벌을 초기화 했다.

```python
# chapter01 code
def __init__(self):
        self._cards = [Card(rank,suit) for suit in self.suits
                       for rank in self.ranks]
```

list comprehension은 한가지 기술만 아는 재주 꾼이다. 다른 종류의 시퀀스를 채우려면 generator expression을 사용해야 한다. 

### 2.2.4 generator expression

튜플 배열 등의 시퀀스 형을 초기화 하려면 list comprehension을 사용할 수도 있지만, 다른 생성자에 전달할 리스트를 통째로 만들지 않고 iterator protocol을  이용해서 항목을 하나씩 생성하는 제너레이터 표현식은 메모리를 더 적게 사용한다.

```python
symbols = '$%#@#'
sym = tuple(ord(symbol) for  symbol in symbols)
print(sym)

import array
sym2 = array.array('I', (ord(symbol) for symbol in symbols))
print(sym2)
'''
1.  generator expression이 함수에 보내는 단 하나의 인수라면 괄호 안에 괄호를 넣을 필요는 없다.
2.  배열  생성자는 인수를 두개 받으므로 generator 앞뒤에 반드시 괄호를 넣어야 한다. 
    배열 생성자는 첫번째 인수는 배열에 들어 갈 숫자들을 저장할 자료형을 지정한다.
'''
```

데카르트 곱에 제네레이터을 사용해서 두 가지 색상과 세 가지 크기의 티 셔츠 목록을 출력한다. list comprehension과 달리 여기서는 티셔츠 리스트의 여섯개 항목을 메모리 안에 생성하지 않는다. generator expression은 한번에 한 항목을 생성할 수 있도록 for 루프에 데이터를 전달하기 때문이다. 

데카르트 곱을 만들기 위해 사용할 리스트에 각각 천개의 항목이 들어가 있는 경우 제네레이터를 사용하면 단지 for루프에 전달하기 위해 항목이 백만 개 들어있는 리스트를  생성하는 일을 피할 수 있다.

```python
colors = ['black','white']
sizes = ['S', 'M', 'L']
for tshirt in ('%s %s'%(c,s) for c in colors for s in sizes):
    print(tshirt)
'''
generator expression은 한번에 하나의 항목을 생성하며, 
6개의 티셔츠 종류를 담고있는 리스트는 만들지 않는다.
'''
```

generator가 작동하는 방식은 chapter14에서 다룬다. 여기서는 단지 리스트 이외의 시퀀스를 초기화하거나 메모리에 유지할 필요가 없는 데이터를 생성하기 위해 generator expression을 사용하는 방법만 보여주였다. 

## 2.3 튜플은 단순한 immutable 리스트가 아니다.

tuple은 불변 리스트로 사용할 수도 있지만 필드명이 없는 레코드로 사용할 수 도 있다. 

### 2.3.1 레코드로서의 튜플

튜플은 레코드를 담고 있다. 튜플은 각 항목은 레코드의 필드 하나를 의미하며 항목의 위치가 의미를 결정한다. 튜플을 단지 immutable list로 생각한다면 경우에 따라 항목의 크기가 순서가 중요할수도 있고 그렇지 않을 수도 있다. 그러나 튜플을 필드의 집합으로 사용하는 경우에는 항목의 수가 고정되어 있고 항목의 순서가 중요하다. 

```python
# LA의 위도와 경도
lax_coordinates = (33.9425, -118.408056)  

# 도쿄에 대한 데이터 (지명 년도, 백만 단위 인구수, 인구 변화율, 단위면적)
city, year, pop, chg, area = ('Tokyo', 2003, 32459,0.66, 8014)

# (국가 코드, 여권번호) 튜플 리스트
traveler_ids = [('USA','31195855'),('BRA','CE324567'),('ESP','XDA31940')] 

for passport in sorted(traveler_ids): # 리스트를 반복할때 passport 변수가 각 튜플에 바인딩 된다.
    print('%s %s' %  passport) # % 포맷 연산자는 튜플을 이해하고 각 항목을 하나의 필드로 처리한다.

# for 루프는 각 항목을 어떻게 가져와야 하는지 알고 있다.(이 과정을 unpacking이라함)
# 여기서 두번째 항목에는 관심이 없으므로 더미변수를 나타내는 _(언더바)를 할당했다.
for country, _ in traveler_ids:
    print(country)
```

튜플은 언패킹 메커니즘 덕분에 레코드로 잘 작동한다. 

### 2.3.2 튜플 unpacking

튜플 언패킹은 iterable 객체라면 어느 객체든 적용할 수 있다. 

튜플 언패킹은 병렬 할당 parallel assignment을 할때 가장 눈에 띈다. 병렬 할당은 다음 코드에서 보는 것처럼 iterable data를 변수로 구성된 tuple에 할당되는 것을 말한다.

```python
lax_coordinates = (33.9425, -118.408056)
latitude, longitude = lax_coordinates
print(latitude)
print(longitude)
```

튜플 언패킹을 이용하면 임시변수를 사용하지 않고도 두 변수의 값을 서로 교환할 수 있다.

```python
b, a = a, b
```

다음과 같이 함수를 호출할때 인수 앞에 *를 붙여 튜플을 언패킹 할수도 있다.

```python
dv = divmod(20,8)
print(dv)
t = (20,8)
print(divmod(*t))
quotient, remainder = divmod(*t)
print(quotient, remainder)
```

함수에서 호출자에 여러 값을 간단히 반환하는 기능이다. 

예를 들어 다음과 같이 os.path.split() 함수를 이용해서 파일 시스템 경로에서 경로명과 파일명을 가져올 수 있다.

```python
import os
_,filename = os.path('/home/luciano/.ssh/idrsa.pub')
print(filename)
```

코드에서 보는것처럼 _와 같은 더미 변수를 placeholder로 사용해서 관심없는 부분은 언패킹할때 무시할 수 있다. 

튜플을 언패킹할 때 일부 항목에만 관심이 있는 경우에는 *를 사용할 수 도 있다. *에 대해 알아보자.

**초과 항목을 잡기위해 * 사용하기**

함수  매개변수에 *를 연결해서 초과된 인수를 가져오는 방법은 파이썬의 고전적인 기능이다.  파이썬3에서는 이 개념을 확장해서 다음과 같은 병렬 할당에도 적용한다.

```python
a, b, *rest = range(5)
print(a,b,rest)
a, b, *rest = range(3)
print(a,b,rest)
a, b, *rest = range(2)
print(a,b,rest)
```

병렬 할당의 경우 *는 단 하나의 변수에만 적용할 수 있다. 하지만 다음과 같이 어떠한 변수에도 적용할 수 있다.

```python
a, *body, c, d = range(5)
print(a,body,c,d)
*head, b, c, d = range(5)
print(head,b,c,d)
```

튜플 언패킹은 내포된 구조체에도 적용할 수 있다는 장점이 있다.

### 2.3.3 내포된 튜플 언패킹

언패킹할 표현식을 받는 튜플은 (a,b,(c,,d)) 처럼 다른 튜플을 내포할 수 있으며, 파이썬은 표현식이 내포된 구조체에 일치하면 제대로 처리한다. 

```python
metro_areas=[
    ('Tokyo','JP',36.933,(35.3224,23.421)),
    ('korea','KR',34.933,(54.3224,53.12)),
    ('USA','US',58.933,(3214,-38.4)),
    ('Mexico city','MX',20.933,(31.244,39.4842)),
]
print('{:15} | {:^9} | {:^9}'.format('','lat.','long.'))
fmt = '{:15} | {:9.4f} | {:9.4f}'
for  name, cc, pop, (latitude,longitude) in metro_areas:
    if longitude>0 :
        print(fmt.format(name,latitude,longitude))
'''
1. 각 튜플은 네개의 필드로 구성된 레코드를 담고 있으며, 마지막 필드는 좌표쌍이다.
2. 마지막 필드를 튜플에 할당함으로써  좌표를 언패킹한다.
3. 이 조건문은 경도가 양인 도시만 출력하게 만든다.
'''
'''
파이썬3이전에는 함수 정의할때 def fn(a,(b,c),d):처럼 매개변수 안에 내포된 튜플을 지정해서 함수를
정의할 수 있었지만, PEP3113-튜플 매개변수 언패킹 제거에서 지원하지 않는다.
'''

```

튜플은 아주 편리하다. 그러나 레코드로 사용하기에는 부족한 점이 있다. 때로는 필드에 이름을 붙일 팔요가 있따. 그래서 nametuple() 함수가 고안되었다. 

### 2.3.4 명명된 튜플

collections.nametuple() 함수는 필드명과 클래스명을 추가한 튜플의 서브클래스를 생성하는 팩토리 함수로서, 디버깅할때 유용하다. 

필드명이 클래스에 저장되므로 nametuple()로 생성한 객체는 튜플과 동일한  크기의 메모리만 사용한다. 속성을 객체 마다 존재하는 __dict__저장하지 않으므로 일반적인  객체  보다 메모리를 더 적게 사용한다. 

```python
from collections import namedtuple
City = namedtuple('City','name country population coordinates')
tokyo = City('Tokyo','JP',36.933,(35.689722,139.691667))
print(tokyo)
print(tokyo.population)
print(tokyo.coordinates)
print(tokyo[1])
'''
1.  명명된 튜플을 정의하려면 클래스명과 필드명의 리스트 총 두개의 매개변수가 필요하다. 
    필드명의 리스트는 반복형 문자열이나 공백으로 구분된 하나의 문자열을 이용해서 지정한다.
2.  데이터는 위치를 맞추고 콤마로 구분해서 생성자에 전달해야 한다.
3.  필드명이나 위치를 이용해서 필드에 접근할 수 있다.
'''
```

명명된 튜플은 튜플에서 상속받은  속성외에 몇가지 속성을 더 가지고 있다. _fields 클래스  속성, _make(iterable) 클래스 메서드, _asdict() 객체 메서드

```python
print(City._fields)
Latlong = namedtuple('LatLong','lat long')
delhi_data = ('Delhi NCR', 'IN', 21.935, Latlong(28.1231,32.4949))
delhi = City._make(delhi_data)
print(delhi._asdict())
for key,value in delhi._asdict().items():
    print(key+':',value)

'''
1. fields는 클래스의 필드명을 담고 있는 튜플이다.
2. _make는 반복형 객체로부터 명명된 튜플을 만든다. City(*delhi_data)를 호출하는 코드와 
동일한 역할을 한다.
3. _asdict()는 명명된 튜플 객체에서 만들어진 collections.OrderedDict 객체를 반환한다.
이 메서드를 이용하면 데이터를 멋지게 출력할 수 있다.
'''
```

지금까지 레코드로 사용할 수있는 튜플의 강력한 기능을 살펴 보았다. 두번째 역할로 불변 리스트 로써의 기능을 알아보자. 

### 2.3.5 immutable list로서의 tuple

튜플을 불변 리스트로 사용할때, 튜플과 리스트가 얼마나 비슷한지 알고 있으면 도움이 된다. _reversed_() 메서드를 제외하고 리스트가 제공하는 메서드를 모두 지원한다.
