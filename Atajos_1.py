from list_base_change import list_base_change
from time import time
import csv


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
        #  if row_check(queens, i) or diagonal_check(queens, i):
        if not( len(queens) == len(set(queens)) ) or diagonal_check(queens, i):
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


n = 8
start_time = time()
old_solutions = [[] for x in range(n)]
queens_solutions = [[]]
j = 0; cc = 0


for i in range((n**n)//2+(n**n)%2):
    # Initialization:
    queens = list_base_change(i, n, n)
    if len(queens) == len(set(queens)): # row checking previous
        queens_solution_member, Err = OneByOne( queens, n)

        if not(Err) and all( queens_solution_member != r for r in old_solutions ):
            print("queens_solution = ", queens_solution_member)
            queens_solutions.append( queens_solution_member )
            #11 old_solutions.append( list(queens_solution) )
            old_solutions.pop(j)
            old_solutions.insert(j, list(queens_solution_member))
            # print("old solution    = ", old_solutions)
            j += 1
            cc += 1
            if j >= n:  # Length of memorized solutions limited at n elements
                j = 0

            queens_solution_member = [(n-1) - r for r in queens_solution_member]  # Sym solution
            print("queens_solution = ", queens_solution_member)
            queens_solutions.append(queens_solution_member)
            #11 old_solutions.append( list(queens_solution) )
            old_solutions.pop(j)
            old_solutions.insert(j, list(queens_solution_member))
            # print("old solution    = ", old_solutions)
            j += 1
            cc += 1
            if j >= n:  # Length of memorized solutions limited at n elements
                j = 0


elapsed_time = time() - start_time
print('\n Transcurridos %0.2f segundos.\n' % elapsed_time)
print( cc, ' solutions.' )


#csvfile = "./queens_solution_"+str(n)+"_"+"time_"+str(int(elapsed_time))+".csv"
#with open(csvfile, "w") as output:
#    writer = csv.writer(output, lineterminator='\n')
#    writer.writerows(queens_solutions)