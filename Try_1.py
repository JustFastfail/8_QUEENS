import random

n = 8  # chessboard size (nxn)

queens = [0] * n  # each element is the row position for each column

# Checkings: ---------------------------------------------------
#   1. Row
#   2. Column (is autochecked, each element belongs to a column)
#   3. Diagonal
#---------------------------------------------------------------


def row_check(queens,column):  # NO-repeated value in the list
        if column == 0:
            return False
        if any(queens[column] == queens[j] for j in range(column)):
            print("Row catch")
            return True
        else:
            return False


def diagonal_check(queens,column):
        if column == 0:
            return False
        if any(queens[column] == queens[column-(j+1)]+(j+1) for j in range(column)) or \
           any(queens[column] == queens[column-(j+1)]-(j+1) for j in range(column)):
            print("Diagonal catch")
            return True
        else:
            return False

i = 0
while i < n:
    print("i= ", i)
    if row_check(queens, i) or diagonal_check(queens, i):
        queens[i] += 1
        print( "Queen = ", queens[i])
        if queens[i] >= n:
            print("Error. Impossible to solve.")
            exit()
    else:
        i += 1


print("The solution is : ", queens)
