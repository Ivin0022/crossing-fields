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
        if (0 <= x < N) and (0 <= y < N):
            cell = arr[x][y]
            if not cell.visited:
                return cell
            else:
                return None

    def check_nearby_squares(self, arr):
        print('checking.....    ')
        self.visited = True

        nearby_squares = [
            self.pre_check(self.x + 1, self.y, arr),  # right
            self.pre_check(self.x, self.y + 1, arr),  # bottom
            self.pre_check(self.x - 1, self.y, arr),  # left
            self.pre_check(self.x, self.y - 1, arr),  # top
        ]

        for sqr in nearby_squares:
            if sqr is not None:
                if abs(sqr.val - self.val) <= H:
                    return sqr


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
    next_square = curent_square.check_nearby_squares(field)
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
