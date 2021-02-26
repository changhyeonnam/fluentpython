# import bisect
# import sys
#
# HAYSTACK = [1, 4, 5, 6, 8, 12, 15, 20, 21, 23, 26, 29, 30]
# NEEDLES = [0, 1, 2, 5, 8, 10, 22, 23, 29, 31, 30]
#
# ROM_FMT = '{0:2d} @ {1:2d}  {2}{0:<2d}'
# def demo(bisect_fn):
#    for needle in reversed(NEEDLES):
#         posistion = bisect_fn(HAYSTACK,needle)
#         offset = posistion* '  |'
#         print(ROM_FMT.format(needle,posistion,offset))
#
# if __name__ =='__main__':
#     if sys.argv[-1] =='left':
#         bisect_fn = bisect.bisect_left
#     else:
#         bisect_fn = bisect.bisect_left
#
# print('DEMO:',bisect_fn.__name__)
# print('haystack ->',' '.join('%2d'% n for n in HAYSTACK))
# demo(bisect_fn)
#
# def grade(score, break_points=[60,70,80,90], grades='FDCBA'):
#     i = bisect.bisect(break_points,score)
#     return grades[i]
# print([grade(score) for score in [33,99,77,70,89,90,100]])
# '''
# 정렬된 긴 숫자 시퀀스를 검색할때 index() 대신 더 빠른 bisect()함수를 사용하는 여러 함수를 보여준다.
# '''