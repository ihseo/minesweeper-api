import random


def create_map(difficulty, width=None, height=None, mines=None):
    import time
    if difficulty == "easy":
        height = 9
        width = 9
        mines = 10
    elif difficulty == "medium":
        height = 16
        width = 16
        mines = 40
    elif difficulty == "hard":
        height = 16
        width = 30
        mines = 99
    elif difficulty == "custom":
        height = height
        width = width
        mines = mines
    else:
        raise Exception("Invalid options")
    minesweeper_map = [[[0, 'C'] for _ in range(height)] for _ in range(width)]
    while mines > 0:  # placing mines
        x = random.randint(0, height - 1)
        y = random.randint(0, width - 1)
        if minesweeper_map[y][x][0] == 0:
            minesweeper_map[y][x][0] = 'X'
            mines -= 1

    for x in range(height):
        for y in range(width):
            if minesweeper_map[y][x][0] == 'X':
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        if (0 <= y + i < width) and (0 <= x + j < height):
                            if minesweeper_map[y + i][x + j][0] != 'X':
                                minesweeper_map[y + i][x + j][0] += 1

    return minesweeper_map


def left_click(minesweeper_map, y, x, is_first_move=False):
    """
    if it's first move and the cell is a mine, move it to another cell
    """
    height = len(minesweeper_map[0])
    width = len(minesweeper_map)
    if is_first_move:
        if minesweeper_map[y][x][0] == 'X':
            count = 0
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if (0 <= y + i < width) and (0 <= x + j < height):
                        if minesweeper_map[y + i][x + j][0] == 'X':
                            count += 1
            minesweeper_map[y][x][0] = 0
            x = random.randint(0, height - 1)
            y = random.randint(0, width - 1)
            # move the mine to another cell (지뢰 이동)
            if minesweeper_map[y][x][0] != 'X':
                minesweeper_map[y][x][0] = 'X'
                for i in range(-1, 2):  # update the number of adjacent cells (지뢰 인접 cell 숫자 업데이트)
                    for j in range(-1, 2):
                        if (0 <= y + i < width) and (0 <= x + j < height):
                            if minesweeper_map[y + i][x + j][0] != 'X':
                                minesweeper_map[y + i][x + j][0] += 1

    if minesweeper_map[y][x][0] == 'X':
        return minesweeper_map, 'over'
    elif minesweeper_map[y][x] == [0, 'C']:
        stack = [(y, x)]
        while stack:  # open the cells (cell 열기)
            y, x = stack.pop()
            minesweeper_map[y][x][1] = 'O'
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if (0 <= y + i < width) and (0 <= x + j < height):
                        if minesweeper_map[y + i][x + j] == [0, 'C']:
                            stack.append((y + i, x + j))
                        else:
                            minesweeper_map[y + i][x + j][1] = 'O'
    else:
        minesweeper_map[y][x][1] = 'O'
    if check_over(minesweeper_map):
        return minesweeper_map, 'clear'
    return minesweeper_map, 'ongoing'


def right_click(minesweeper_map, y, x):
    """
    :param minesweeper_map: 2d list
    :param y: int (y coordinate)
    :param x: int (x coordinate)
    :return: 2d list (updated map)
    """
    if minesweeper_map[y][x][1] == 'C':
        minesweeper_map[y][x][1] = 'F'
    elif minesweeper_map[y][x][1] == 'F':
        minesweeper_map[y][x][1] = 'C'
    return minesweeper_map


def left_right_click(minesweeper_map, y, x):
    """
    If the number equals the flags on the adjacent cells,
    check if they are indeed mines. If so, open the cells.
    :param minesweeper_map: 2d list
    :param y: int (y coordinate)
    :param x: int (x coordinate)
    :return: 2d list (updated map)
    """
    height = len(minesweeper_map[0])
    width = len(minesweeper_map)
    if minesweeper_map[y][x][1] == 'O':
        count = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if (0 <= y + i < width) and (0 <= x + j < height):
                    if minesweeper_map[y + i][x + j][1] == 'F':  # count the flags (flag 개수 세기)
                        if minesweeper_map[y + i][x + j][0] != 'X':
                            # if the flag is not on a mine, return (지뢰가 아닌 flag가 있으면 return)
                            return minesweeper_map, 'over'
                        count += 1
        if count == minesweeper_map[y][x][0]:
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if (0 <= y + i < width) and (0 <= x + j < height):
                        if minesweeper_map[y + i][x + j][1] == 'C':
                            # open the cells (cell 열기)
                            minesweeper_map = left_click(minesweeper_map, y + i, x + j)
    if check_over(minesweeper_map):
        return minesweeper_map, 'clear'
    return minesweeper_map, 'ongoing'


def print_map(minesweeper_map):
    height = len(minesweeper_map[0])
    width = len(minesweeper_map)
    for x_ in range(height):
        for y_ in range(width):
            print(minesweeper_map[y_][x_], end=' ')
        print()


def check_over(minesweeper_map):
    height = len(minesweeper_map[0])
    width = len(minesweeper_map)
    for x in range(height):
        for y in range(width):
            if minesweeper_map[y][x][0] != 'X' and minesweeper_map[y][x][1] == 'C':
                return False
    return True