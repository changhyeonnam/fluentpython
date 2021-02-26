# ch02_sequence(2)

Created: Feb 26, 2021 1:15 PM

### 2.4 슬라이싱

### 2.4.2 슬라이싱 객체

seq[start:stop:step] 표현식을 평가하기 위해 seq.__getitem__(slice,stop,step))을 호출한다. 시퀀스 형을 직접 구현하지 않아도 슬라이스 객체를 알아두면 도움이 된다. 슬라이스  객체에 이름을 붙일 수 있다. 코드에서 슬라이스를 하드코딩 하는 대신 각 슬라이스에  이름을 붙일 수 있다. for루프의 가독성이 좋아진다. 

### 2.4.3 다차원 슬라이싱 생략 기호

[ ]연산자는 콤마로 구분해서 여러개의 인덱스나 슬라이스를 가질 수 있다. a[m:n, k:1] 구문으로 2차원 슬라이스 가져올 때 사용할 수 있다. [ ] 연산자를 처리하는  __getitem__() 과 __setitem__() 특수 메서드는 a[i,j]에 들어 있는 인덱스들을 튜플로 받는다. 

Numpy는 다차원 배열을 슬라이싱할때 생략기호(...)를 사용한다.  x[ i, ..] = x[ i, :, :, :]와 같다. 

슬라이스는 시퀀스에서 정보를 추출할때 뿐만 아니라 mutable 시퀀스의 값을 변경할 때도 사용할 수 있다.

### 2.4.4 슬라이싱에 할당하기

```python
l = list(range(10))
print(l)
l[2:5] = [20,30]
print(l)
del l[5:7]
print(l)
```

### 2.5 시퀀스에 덧셈과 곱셈 연산자 사용하기

덧셈의 경우 피 연산자 두개가 같은 자료형이여야 하고, 둘 다 변경되지 않지만 동일한 자료형의 시퀀스가 새로 만들어 진다. 덧셈 및  곱셈 연산자는 언제나 객체를  새로 만들고, 피 연산자는 변경하지 않는다. 

### 2.5.1 리스트의 리스트 만들기

```python
board  = [['_'] *3 for i in range(3)]
print(board)
board[1][2] = 'X'
print(board)
# 위의 코드는 실제로 아래처럼 동작.
board=[]
for i in range(3):
    row = ['_']*3
    board.append(row)

weird_board = [['_']*3]*3
print(weird_board)
weird_board[1][2]='0'
print(weird_board)
# 세개의 행이 모두 동일한 객체를 참조 하고 있다.
# 위의 코드는 실제로 아래처럼 동작
weird_row = ['_'] * 3
weird_board = []
for i in range(3):
    weird_board.append(weird_row)
```

### 2.6  시퀀스의 복합 할당

+=과 *= 등의 복합 할당 연산자는 첫번째 피 연산자에 따라 다르게 작동한다. 

+= 연산자가 작동하도록 만드는 특수 메서드는 __iadd__()다. 그런데 __iadd__() 메서드가 구현되어 있지 않다면, 파이썬은 대신 __add__() 메서드를 호출한다. __iadd__()가 구현되어 있다면 a+=b에서 a값이 변경된다. 그런데 구현되어 있지 않다면 a+=b 표현식은 a+b를 먼저 평가하고 객체를 새로 생성한 후에 a에 할당한다. __iadd__()  구현에 따라 a 변수가 가르키는 객체의 정체성이 바뀔 수 도있고 그렇지 않을  수 도 있다. 

```python
l = [1,2,3]
print(l)
print(id(l))
l *= 2
print(l)
print(id(l))

t = (1,2,3)
print(id(t))
print(t)
t*=2
print(id(t))
print(t)
```

mutable sequence에 대해서 __iadd()__ 메서드를 구현해서 += 연산자가 기존 객체의 내용을 변경하게 만드는 것이 좋다. immutable sequence의 경우에 이 연산을 수행할 수 없다. 

새로운 항목을 추가하는 대신 항목이 추가된 시퀀스 객체를 새로 만들어 타깃 변수에 저장하므로, Immutable 시퀀스에 반복적으로 연결 연산하는 것은 비 효율적이다.

### 2.6.1 += 복합 할당 퀴즈

```python
quiz
t = (1,2,[30,40])
t[2] += [50,60]
print(t)
# 지금은 안돌아 가네.. python 3.9, 3.5에서는 돌아갔다고 함.
```

s[a] += b 표현식에 대해 파이썬이 생성한 바이트 코드를 살펴보자.

```python
							0 LOAD_NAME                0 (s)
              2 LOAD_NAME                1 (a)
              4 DUP_TOP_TWO
              6 BINARY_SUBSCR
              8 LOAD_NAME                2 (b)
             10 INPLACE_ADD
             12 ROT_THREE
             14 STORE_SUBSCR
             16 LOAD_CONST               0 (None)
             18 RETURN_VALUE
```

1. s[a] 값을 스택의 꼭대기 (Top of Stack)(ToS)에 놓는다.
2. TOS += b 연산을 수행한다. TOS가 가변객체를 가리키면 이 연산은 성공한 것이다.
3. TOS를 s[a]에 할당한다. s가 불변 객체면 이 연산은 실패한다. 

요약

1. 가변 항목을 튜플에 넣는 것은 좋은 생각이 아니다.
2. 복합  할당은 원자적인 연산이 아니다. 
3. 파이썬 바이트코드를 살펴보는 것은 그리 어렵지 않으며, 내부에서 어떤 일이 발생하고 있는지 살펴보는데 도움이 된다. 

### 2.7 list.sort()와 sorted() 내장함수

list.sort() 메서드는 사본을 만들지 않고 리스트 내부를 변경해서 정렬한다. sort() 메서드는 타깃 객체를 변경하고 새로운 리스트를 생성하지 않았음을 알려주기 위해 None을 반환한다. 이것은 파이썬 API의 중요한 관례다. 객체를 직접 변경하는 함수나 메서드는 객체가 변경되었고 새로운 객체가 생성되지 않았음을 호출자에 알려주기 위해 None을 반환해야한다. random.shuffle()함수도 이와 동일하게 동작한다.

이와 반대로 sorted() 내장 함수는 새로운 리스트를  생성해서 반환한다. 사실 sorted()는 불변 시퀀스 및 제너레이터를 포함해서 반복가능한 모든 객체를  인수로 받을 수 있다. 

입력받은 반복가능한 객체의 자료형과 무관해서 sorted()함수는 언제나 새로 생성한 리스트를 반환한다.

list.sort() 메서드와 sorted함수 모두 선택적으로 두개의 키워드를 받는다. 

- reverse : 참이면 내림차순 반환
- key : 정렬에 사용할 키를 생성하기 위해 각 항목에 적용할 함수를 인수로 받는다. ex) key= str.lower, key=len.

```python
fruit = ['grape','rasberry','apple','banna']
print(sorted(fruit))
print(fruit)
print(sorted(fruit,reverse=True))
print(sorted(fruit,key=len))
print(sorted(fruit,reverse=True,key=len))
print(fruit)
print(fruit.sort())
print(fruit)
'''
['apple', 'banna', 'grape', 'rasberry']
['grape', 'rasberry', 'apple', 'banna']
['rasberry', 'grape', 'banna', 'apple']
['grape', 'apple', 'banna', 'rasberry']
['rasberry', 'grape', 'apple', 'banna']
['grape', 'rasberry', 'apple', 'banna']
None
['apple', 'banna', 'grape', 'rasberry']
'''
```

### 2.8 정렬된 시퀀스를  bisect로 관리하기

bisect 모듈은 bisect()와 insort() 함수를 제공한다. bisect()는 이진 검색 알고리즘을 이용해서 시퀀스를 검색하고,  insort()는 정렬된 시퀀스안에 항목을 삽입한다.

### 2.8.1 bisect()로 검색하기

bisect(haystack, needle)은 정렬된  시퀀스인 haystack 안엥서 오름차순 정렬 사앹를 유지한 채로 needle을 추가할 수 있는  위치를 찾아낸다. 즉 해당 위치 앞에는 needle 보다 같거나 작은 항목이 온다. bisect(haystack, needle)의 결과값을 인덱스(index)로 사용해서 haystack.insert( index,  needle)을 호출하면 needle을 추가할 수 있지만 insort() 함수는 이 두과정을  더 빨리 처리한다. 

```python
import bisect
import sys

HAYSTACK = [1, 4, 5, 6, 8, 12, 15, 20, 21, 23, 26, 29, 30]
NEEDLES = [0, 1, 2, 5, 8, 10, 22, 23, 29, 31, 30]

ROM_FMT = '{0:2d} @ {1:2d}  {2}{0:<2d}'
def demo(bisect_fn):
   for needle in reversed(NEEDLES):
        posistion = bisect_fn(HAYSTACK,needle)
        offset = posistion* '  |'
        print(ROM_FMT.format(needle,posistion,offset))

if __name__ =='__main__':
    if sys.argv[-1] =='left':
        bisect_fn = bisect.bisect_left
    else:
        bisect_fn = bisect.bisect

print('DEMO:',bisect_fn.__name__)
print('haystack ->',' '.join('%2d'% n for n in HAYSTACK))
demo(bisect_fn)
'''
DEMO: bisect_right
haystack ->  1  4  5  6  8 12 15 20 21 23 26 29 30
30 @ 13    |  |  |  |  |  |  |  |  |  |  |  |  |30
31 @ 13    |  |  |  |  |  |  |  |  |  |  |  |  |31
29 @ 12    |  |  |  |  |  |  |  |  |  |  |  |29
23 @ 10    |  |  |  |  |  |  |  |  |  |23
22 @  9    |  |  |  |  |  |  |  |  |22
10 @  5    |  |  |  |  |10
 8 @  5    |  |  |  |  |8 
 5 @  3    |  |  |5 
 2 @  1    |2 
 1 @  1    |1 
 0 @  0  0

DEMO: bisect_left
haystack ->  1  4  5  6  8 12 15 20 21 23 26 29 30
30 @ 12    |  |  |  |  |  |  |  |  |  |  |  |30
31 @ 13    |  |  |  |  |  |  |  |  |  |  |  |  |31
29 @ 11    |  |  |  |  |  |  |  |  |  |  |29
23 @  9    |  |  |  |  |  |  |  |  |23
22 @  9    |  |  |  |  |  |  |  |  |22
10 @  5    |  |  |  |  |10
 8 @  4    |  |  |  |8 
 5 @  2    |  |5 
 2 @  1    |2 
 1 @  0  1 
 0 @  0  0
'''
```

1. 삽입 위치를 찾아내기 위해 선택한 bisect 함수를 사용한다.
2. 간격에 비례해서 수직 막대 패턴을 만든다.
3. needle과 삽입 위치를 보여주는 포맷된 행을 출력한다.
4. 마지막 명령해 인수에 따라 사용할 bisect 함수를 선택한다.
5. 선택된 함수명을 헤더에 출력한다. 

bisect의 행동은 두가지 방식으로 조절할 수 있다.

1. 선택인수인 lo와  hi를 사용하면 삽입할 때 검색할  시퀀스 영역을 좁힐 수 있다. lo의 기본값은 0, hi 기본값은 len()이다.
2. 둘째 bisect는  실제로 bisect_right() 함수의 별명이다. 

bisect_right()는 기존 항목 바로 뒤를 삽입 위치로 반환하며  bisect_left()는 기존항목 위치를 삽입 위치로 반환하므로 기존 항목 바로 앞에 삽입된다. 

```python
def grade(score, break_points=[60,70,80,90], grades='FDCBA'):
    i = bisect.bisect(break_points,score)
    return grades[i]
print([grade(score) for score in [33,99,77,70,89,90,100]])
'''
정렬된 긴 숫자 시퀀스를 검색할때 index() 대신 더 빠른 bisect()함수를 사용하는 여러 함수를 보여준다.
'''
```

### 2.8.2 bisect.insrt()로 삽입하기

정렬은 값비싼 연산이므로 시퀀스를 일단 정렬한 후에는 정렬  상태를 유지하는것이 좋다. 그렇기 때문에 bisect.insort() 함수가 만들어 졌다. 

insort(seq,item)은 seq를 오름차순으로 유지한 채로 item을 seq에 삽입한다. 

```python
import bisect
import random

SIZE = 7
random.seed(1729)

my_list = []
for i in range(SIZE):
    new_item = random.randrange(SIZE*2)
    bisect.insort(my_list,new_item)
    print('%2d ->' % new_item,my_list)
```

bisect 함수와 마찬가지로 insort  함수도 선택적으로 lo와  hi 변수를 인수로 받아 시퀀스 안에서 검색할 범위를 제한한다. 그리고 삽입 위치를 검색하기 위해 bisect_left() 함수를 사용하는 insort_left() 함수도 있다. 

### 2.9 리스트가 답이 아닐 때

실수가 천만개 저장해야 할 때는 배열이 훨씬 더 효율 적이다. 배열은 모든 기능을 갖춘 float 객체  대신 C언어의 배열과 마찬가지로 기계가 사용하는 형태로 표현된 바이트 값만을 저장한다. 리스트의 양쪽 끝에 항목을 계속 추가, 삭제 시엔 deque가 좋다. (FIFO, LIFO 지원)

### 2.9.1 배열

리스트안에  숫자만 있다면 배열이 리스트보다 훨씬 더 효율적이다. 모든 연산을 지원 하며, 빠르게 파일이 저장하고 읽어 올수 있는 frombytes()와  tofile() 메서드도 추가로  제공한다. 

파이썬 배열은 C배열만큼 가볍다. 배열 생성시 배열에 저장되는 각항목의 C 기반 형을 결정하는 문자인 typecode를 지정한다. signed char에 대한 bytecode는 b다. array('b') 배열을  생성하면 각 항목은 하나의 바이트로 저장되고 -128에서  127까지의 정수로 해석된다. 숫자가 아주 많이 들어 있는 시퀀스의 경우 배열에 저장하면 메모리가 많이 절약된다. 파이썬은 배열 형에 숫자를  저장할  수 없게 한다.

```python
from array import array
from random import random

floats = array('d',(random() for i in range(10**7)))
print(floats[-1])
fp = open('floats.bin','wb')
floats.tofile(fp)
fp.close()
floats2 = array('d')
fp = open('floats.bin','rb')
floats2.fromfile(fp, 10**7)
fp.close()
print(floats2[-1])
print(floats2 == floats)

'''
0.17509744104934566
0.17509744104934566
True
'''
```

텍스트  파일에서 숫자를 읽어오는것보다  60배 빠르고, 크기도 2배 넘게 아낄수 있다. tofile(),fromfile() 메서드가 0.1초정도 차이난다. 

이진 데이터를 표현하는 숫자 배열을 위해 파이썬에서는 bytes와 bytearray 형을 제공한다. 

### 2.9.2 메모리 뷰

메모리 뷰 (memory view) 내장 클래스는 공유 메모리 시퀀스형으로 써 bytes를 복사하지 않고 배열의 슬라이스를 다룰 수 있게 해준다. 이 클래스는 numpy에서 영감을 받아 만들었다. 

numpy의  개발자 올리판트는 '언제 메모리 뷰를 사용해야 하는가?'에 대해 메모리 뷰는 본질적으로 파이썬 자체에 들어있는 NumPy 배열 구조체를 일반화한것이다. 메모리  뷰는  PIL 이미지, SQLlite 데이터베이스, Numpy 배열 등 데이터 구조체를 복사하지 않고 메모리를 공유할  수 있게 해준다. 데이터 셋이 커지는 경우  이것은 아주 중요한  기법이다. 

```python
import array

numbers = array.array('h',[-2,-1,0,1,2])
memv = memoryview(numbers)
print(len(memv))
print(memv[0])
print(memv_oct.tolist())
memv_oct[5] = 4
print(numbers)
'''
5
-2
[254, 255, 255, 255, 0, 0, 1, 0, 2, 0]
array('h', [-2, -1, 1024, 1, 2])
'''
```

### 2.9.3 Numpy와 Scipy

Numpy는 숫자뿐만 아니라 사용자 정의 레코드도 저장할  수 있는  다차원 동형  배열 및 행렬을 구현하고 요소 단위에서 효율적으로 계산할 수 있게 해준다.

SciPy는 NumPy를 기반으로 작성된 라이브러리로서, 선형대수학, 수치해석, 통계학에 나오는 여러 과학 계산 알고리즘을 제공한다. SciPy는 C및 포트란 코드 기반을 활용함 으로써 빠르고 신뢰성이 높다. 

```python
import numpy
a = numpy.arange(12)
print(a)
print(type(a))
print(a.shape)
a.shape = 3,4
print(a)
print(a[2])
print(a[2,1])
print(a[:,1])
print(a.transpose())
'''
[ 0  1  2  3  4  5  6  7  8  9 10 11]
<class 'numpy.ndarray'>
(12,)
[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]]
[ 8  9 10 11]
9
[1 5 9]
[[ 0  4  8]
 [ 1  5  9]
 [ 2  6 10]
 [ 3  7 11]]
'''
```

2.9.4 deque 및 기타 queue

append()와 pop() 메서드를 사용해서 리스트를 스택이나 큐로 사용할 수 있다. 그러나 왼쪽에 삽입하거나 삭제하는 연산은 전체 연산은 리스트를 이동시켜야 하므로 처리 부담이 크다.

덱 클래스는 큐의 양쪽 어디에서든 빠르게 삽입 및 삭제할 수 있도록 설계된 thread-safe 양방향 큐다.

```python
from collections import deque
dq = deque(range(10),maxlen=10)
print(dq)
dq.rotate(3)
print(dq)
dq.rotate(-4)
print(dq)
dq.appendleft(-1)
print(dq)
dq.extend([11,22,33])
print(dq)
dq.extendleft([10,20,30,40])
print(dq)
'''
deque([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], maxlen=10)
deque([7, 8, 9, 0, 1, 2, 3, 4, 5, 6], maxlen=10)
deque([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], maxlen=10)
deque([-1, 1, 2, 3, 4, 5, 6, 7, 8, 9], maxlen=10)
deque([3, 4, 5, 6, 7, 8, 9, 11, 22, 33], maxlen=10)
deque([40, 30, 20, 10, 3, 4, 5, 6, 7, 8], maxlen=10)
'''
```

덱은  리스트 메서드 대부분을 구현할 뿐만 아니라 popleft()와 rotate()처럼 고유한 메서드를 추가로 가지고 있다. 그렇지만  숨은 단점도 있다. 덱의 중간 항목을  삭제하는 연산은 그리 빠르지 않다. 덱이 양쪽 끝에 추가나 제거하는 연산에 최적화되어 있기 때문이다.

append()와 popleft() 메서드는 원자성을  가지고 있으므로 멀티 쓰레드 앱에서 락을 사용하지 않고 덱을 이용해서 간단한 FIFO 큐를 구현할 수 있다.