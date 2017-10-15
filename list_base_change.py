# -*- coding: utf-8 -*-
# !/usr/bin/python

# nelementos is the number of elements for the binary
def list_base_change(decimal, base, nelementos):

    binario = []
    #base = 4

    while decimal // base != 0:
        binario = [decimal % base] + binario
        decimal = decimal // base
    binario = [decimal] + binario
    binario = [0] * (nelementos - len(binario)) + binario
    return binario


# n = 8
# for i in range(n**n):
#     print( list_base_change(i, n, n) )



# print(list_base_change(7, 2, 8))