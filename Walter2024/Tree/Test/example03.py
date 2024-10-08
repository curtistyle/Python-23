matrix = [
   # x  x  x
    [1, 2, 3], #y_1
    [4, 5, 6], #y_2
    [7, 8, 9]  #y_3
    ]

def limite (m, x, y):
    def inY(m, x, y):
        if (x >= 0) and (len(m[0]) < x):
            return True
        else:
            return False
    def inX(m, x, y):
        if (y >= 0) and (len(m) < y):
            return True
        else:
            return False
    return True if inY(m, x, y) and (inX(m, x, y)) else False

def existe(mat, value, x=0,y=0):
    if (value == mat[y][x]):
        return True
    else:
        # derecha
        if x >= 0 and x < len(mat[0]):
            pass


x = 1
y = 3

print(matrix[x-1][y-1])