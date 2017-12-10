from list_base_change import list_base_change_np
from time import time
import numpy as np
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
        if not( queens.size == np.unique(queens).size ) or diagonal_check(queens, i):
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
old_solutions = np.zeros((n,n))
queens_solutions = np.array([])
j = 0; cc = 0


for i in range((n**n)//2+(n**n)%2):
    # Initialization:
    queens = list_base_change_np(i, n, n)
    if queens.size == np.unique(queens).size : # row checking previous
        #11 print('posible solucion')
        #11 print(queens)
        queens_solution_member, Err = OneByOne( queens, n)
        #11 print('q', queens_solution_member, Err)
        #11 print('a', old_solutions[:,:] )

        if not(Err) and not(all(  [np.array_equal(queens_solution_member, old_solutions[r,:]) for r in range(n)] )) :
            print("queens_solution = ", queens_solution_member)
            queens_solutions = np.concatenate((queens_solutions, queens_solution_member) )
            #11 old_solutions.append( list(queens_solution) )
            old_solutions[j,:] = queens_solution_member
            #11 print("old solution    = ")
            #11 print( old_solutions)
            j += 1
            cc += 1
            if j >= n:  # Length of memorized solutions limited at n elements
                j = 0

            queens_solution_member = np.array([(n-1) - r for r in queens_solution_member])  # Sym solution
            print("queens_solution = ", queens_solution_member)
            queens_solutions = np.concatenate((queens_solutions, queens_solution_member))
            #11 old_solutions.append( list(queens_solution) )
            old_solutions[j, :] = queens_solution_member
            #11 print("old solution    = ")
            #11 print( old_solutions )
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