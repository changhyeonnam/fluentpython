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

