class square():
    def __init__(self, x, y, val):
        self.x = x
        self.y = y
        self.val = val
        self.visited = False

    def __str__(self):
        return '(' + str(self.x) + ', ' + str(self.y) + ') -> ' + str(self.val)


class field():
    def __init__(self, val, N, H):
        self.arr = []
        self.N = N
        self.H = H

        for j in range(N):
            for i in range(N):
                self.arr.append(square(i, j, val[i + j * N]))

    def pre_check(self, x, y):
        if (0 <= x < self.N) and (0 <= y < self.N):
            cell = self.arr[x + y * self.N]
            if not cell.visited:
                return cell
            else:
                return None

    def check_nearby_squares(self, cell):
        print('checking.....    ' + str(cell), end='    \n')
        cell.visited = True

        nearby_squares = [
            self.pre_check(cell.x + 1, cell.y),  # right
            self.pre_check(cell.x, cell.y + 1),  # bottom
            self.pre_check(cell.x - 1, cell.y),  # left
            self.pre_check(cell.x, cell.y - 1),  # top
        ]

        for sqr in nearby_squares:
            if sqr is not None:
                if abs(sqr.val - cell.val) <= self.H:
                    return sqr

    def walk(self):

        stack = []

        curent_square = self.arr[0]

        while True:
            next_square = self.check_nearby_squares(curent_square)

            if curent_square.x == self.N - 1 and curent_square.y == self.N - 1:
                print('yes')
                break

            if next_square is None:
                curent_square = stack.pop()
            else:
                stack.append(curent_square)
                curent_square = next_square


if __name__ == '__main__':

    field_vals = [

        3, 6, 4, 9,
        7, 1, 2, 3,
        6, 7, 2, 2,
        7, 7, 1, 5,
    ]

    f = field(field_vals, 4, 3)
    f.walk()
