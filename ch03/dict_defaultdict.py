'''
default 객체를 생성할 때 존재하지 않는 키 인수로 __getitem__() 메서드를 호출할때 마다 기본 값을 생성하기 위해 사용되는 콜러블 제공
'''

import sys
import re
import collections

WORDE_RE = re.compile(r'\w+')
# default_factory에 list 생성자를 갖고있는 defaultdict을 생성한다.
index = collections.defaultdict(list)

with open(sys.argv[1], encoding='utf-8') as fp:
    for line_no, line in enumerate(fp,1):
        for match in WORD_RE.finditer(line):
            word = match.group()
            column_no = match.start() +1
            location = (line_no,column_no)
            index[word].append(location)
'''
    word가 index에 들어있지 않으면 default-factory를 호출해서 없는 값에 대한 항목을 생성하는데,
    여기서는 빈 리스트를 생성해서 index[word]에 할당한 후 반환하므로, append(location) 연산은 언제나 성공한다.  
'''
for word in sorted(index, key= str.upper):
    print(word, index[word])
