import random
from collections import namedtuple
RandomValue = namedtuple("RandomValue", ("Value", "RowIndex", "ValueIndex"))


class Matrix():
    def __init__(self, cols, rows):
        self.cols = cols
        self.rows = rows

        self.matrix = []
        for i in range(rows):
            selec_row = []
            for j in range(cols):
                selec_row.append(0)
            self.matrix.append(selec_row)

    def setitem(self, col, row, v):
        self.matrix[col - 1][row - 1] = v

    def randSelect(self):
        row = self.matrix[random.randrange(len(self.matrix))]
        value = random.choice(row)
        return RandomValue(value, self.matrix.index(row), row.index(value))

    def __repr__(self):
        outStr = ""
        for i in range(self.rows):
            outStr += 'Row %s = %s\n' % (i + 1, self.matrix[i])
        return outStr

a = Matrix(3, 3)
R = 3
C = 3

# For user input
for i in range(R):  # A for loop for row entries
    a = []
    for j in range(C):  # A for loop for column entries
        if (j % 2 == 0):
            a.append(1, 2, int(input()))

print(random_val.RowIndex)
print(random_val.ValueIndex)
print(random_val.Value)
