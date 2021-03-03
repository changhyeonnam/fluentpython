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