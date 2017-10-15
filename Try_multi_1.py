import multiprocessing.dummy as mp
import itertools
from list_base_change import list_base_change
from time import time

# Checkings: ---------------------------------------------------
#   1. Row
#   2. Column (is autochecked, each element belongs to a column)
#   3. Diagonal
#---------------------------------------------------------------


def row_check(queens,column):  # NO-repeated value in the list
        if column == 0:
            return False
        if any(queens[column] == queens[j] for j in range(column)):
            #print("Row catch")
            return True
        else:
            return False


def diagonal_check(queens,column):
        if column == 0:
            return False
        if any(queens[column] == queens[column-(j+1)]+(j+1) for j in range(column)) or \
           any(queens[column] == queens[column-(j+1)]-(j+1) for j in range(column)):
           # print("Diagonal catch")
            return True
        else:
            return False


def OneByOne( queens, n ):
    error = False
    i = 0
    while i < n:
        #print("i= ", i)
        if row_check(queens, i) or diagonal_check(queens, i):
            queens[i] += 1
            #print( "Queen = ", queens[i])
            if queens[i] >= n:
                #print("Error. Impossible to solve.")
                error = True
                break
                #return queens, error
        else:
            i += 1
    return queens, error


n= 4
start_time = time()
global old_solutions
old_solutions = [[] for x in range(n)]
global j
j = 0

##for i in range(n**n):
def Initialization(i=0, n=8):
    queens = list_base_change(i, n, n)
    queens_solution, Err = OneByOne( queens, n)
    if globals()["j"] >= n:  # Length of memorized solutions limited at n elements
        globals()["j"] = 0
    # if not(Err) and j == 0:
    #     print("queens_solution = ", queens_solution)
    #     #11 old_solutions.append(list(queens_solution))
    #     old_solutions.pop(j)
    #     old_solutions.insert(j, list(queens_solution))
    #     print("old solution    = ", old_solutions)
    #     j += 1
    # else:

    if not(Err) and all( queens_solution != r for r in globals()["old_solutions"] ):
        print("queens_solution = ", queens_solution)
        #11 old_solutions.append( list(queens_solution) )
        globals()["old_solutions"].pop(j)
        globals()["old_solutions"].insert(j, list(queens_solution))
        # print("old solution    = ", old_solutions)
        globals()["j"] += 1
        # print("Err = ",  Err)

        return queens_solution

    else:
        if i >= n**n: return
        Initialization(i+1, n)

# p = mp.Pool(4)
# Sol = p.map(Initialization, range(n**n))
# for r in Sol:
#     print(r)
# p.close()
# p.join()

Initialization(0)

elapsed_time = time() - start_time
print('\n Transcurridos %0.2f segundos.\n' % elapsed_time)