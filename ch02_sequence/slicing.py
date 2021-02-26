l = [10,20,30,40,50,60]
print(l[:2])
print(l[2:])
print(l[:3])
print(l[3:])
# x 인덱스를 기준으로 겹침없이 시퀀스를 분할하기 쉽다.

s = 'bicycle'
print(s[::3])
print(s[::-1])
print(s[::-2])

import collections
from  random  import choice
Card = collections.namedtuple('Card',['rank','suit'])
class  FrenchDeck:
    ranks = [str(n) for n in range(2,11)] + list('JQKA')
    suits = 'spades  diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank,suit) for suit in self.suits
                       for rank in self.ranks]
    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

deck = FrenchDeck()
print(deck[12::13])

l = list(range(10))
print(l)
l[2:5] = [20,30]
print(l)
del l[5:7]
print(l)