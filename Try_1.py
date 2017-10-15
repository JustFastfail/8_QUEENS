import random
from list_base_change import list_base_change

#n = 8  # chessboard size (nxn)

#queens = [4,0,0,0,0,0,0,0] #[1] * n  # each element is the row position for each column

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


def OneByOne( queens, n ):
    error = False
    i = 0
    while i < n:
        print("i= ", i)
        if row_check(queens, i) or diagonal_check(queens, i):
            queens[i] += 1
            print( "Queen = ", queens[i])
            if queens[i] >= n:
                print("Error. Impossible to solve.")
                error = True
                return error
        else:
            i += 1
    return queens, error


n = 8
queens = [0] * n
queen_possible_value = range(n)


def Permutation(list, column, nmax):
    for i in range(nmax):
        list[column] = i
        list, Err = OneByOne( list, nmax)
        if Err:
            Permutation(list, column+1, nmax)
        else:
            break



# if Err:
#     print("No solution encountered!")


