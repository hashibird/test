def flipable(y, x, player):
    enemy = 1 if player == 0 else 0
    for dy, dx in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
        depth, flg = 1, 0
        for i in range(size):
            ry, rx = y + (dy * depth), x + (dx * depth)
            if any([rx <= -1, ry <= -1, rx >= size, ry >= size]):
                break
            if board[ry][rx] is None:
                break
            elif flg == 0 and board[ry][rx] == player:
                break
            elif flg == 0 and board[ry][rx] == enemy:
                flg = 1
            elif flg == 1 and board[ry][rx] == player:
                return True
            depth += 1
    return False

def flip_stone(y, x, player):
    if board[y][x] is not None:
        return False
    if not flipable(y, x, player):
        return False


    else:
        enemy = 1 if player == 0 else 0
        result = [(y, x)]
        for dy, dx in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
            depth, flg = 1, 0
            tmp = []
            for i in range(size):
                ry, rx = y + (depth * dy), x + (depth * dx)
                if any([rx <= -1, ry <= -1, rx >= size, ry >= size]):
                    break
                if board[ry][rx] is None:
                    break
                elif flg == 0 and board[ry][rx] == player:
                    break
                elif flg == 0 and board[ry][rx] == enemy:
                    flg = 1
                    tmp.append((ry, rx))
                elif flg == 1 and board[ry][rx] == enemy:
                    tmp.append((ry, rx))
                elif flg == 1 and board[ry][rx] == player:
                    result += tmp
                    break
                depth += 1

        for y2, x2 in result:
            board[y2][x2] = player
        return True

def print_board():
    print('', end='\t')
    for x0 in range(size):
        print('X:{0}'.format(x0), end='\t')
    print()
    for y1, b in enumerate(board):
        print('Y:{0}'.format(y1), end='\t')
        for s in b:
            print('' if s is None else s, end='\t')
        print()

size, black, white = 8, 1, 0

board = [[None for i in range(size)] for i in range(size)]
board[3][3], board[3][4], board[4][3], board[4][4] = white,black,black,white
    
print_board()
print(flipable(3,2,1))
print_board()
print('end')

print('test')


