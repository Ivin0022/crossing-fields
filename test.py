N, H = (4, 3)

field_vals = [

    [3, 6, 4, 9],
    [7, 1, 2, 3],
    [6, 7, 2, 2],
    [7, 7, 1, 5],
]


class square():
    def __init__(self, x, y, val):
        self.x = x
        self.y = y
        self.val = val
        self.visited = False

    def __str__(self):
        return '(' + str(self.x) + ', ' + str(self.y) + ') -> ' + str(self.val)

    def pre_check(self, x, y, arr):
        cell = arr[x][y]
        if (0 <= x < N) and (0 <= y < N):
            return cell
        else:
            return self

    def check_nearby_square(self, arr):
        print('checking.....    ')
        self.visited = True
        # right
        if (self.x + 1) < N:
            right = arr[self.x + 1][self.y]
            if abs(right.val - self.val) <= H and not right.visited:
                print('right  -  ', end='')
                return right

        # bottom
        if (self.y + 1) < N:
            bottom = arr[self.x][self.y + 1]
            if abs(bottom.val - self.val) <= H and not bottom.visited:
                print('bottom  -  ', end='')
                return bottom

        # left
        if (self.x - 1) >= 0:
            left = arr[self.x - 1][self.y]
            if abs(left.val - self.val) <= H and not left.visited:
                print('left  -  ', end='')
                return left

        # top
        if (self.y - 1) >= 0:
            top = arr[self.x][self.y - 1]
            if abs(top.val - self.val) <= H and not right.visited:
                print('top  -  ', end='')
                return top


field = []
stack = []

for i in range(N):
    temp = []
    for j in range(N):
        val = field_vals[i][j]
        temp.append(square(i, j, val))
    field.append(temp)

curent_square = field[0][0]

while True:
    next_square = curent_square.check_nearby_square(field)
    print(curent_square)

    if not (curent_square.x == N - 1 and curent_square.y == N - 1):
        pass
    else:
        input('yes')
        break

    if next_square is None:
        curent_square = stack.pop()
    else:
        stack.append(curent_square)
        curent_square = next_square
