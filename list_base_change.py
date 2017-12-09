# -*- coding: utf-8 -*-
# !/usr/bin/python

import numpy as np

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

def list_base_change_np(decimal, base, nelementos):

    binario = np.array([])
    # base = 4

    while decimal // base != 0:
        binario = np.concatenate(([decimal % base], binario))
        decimal = decimal // base
    binario = np.concatenate(([decimal], binario))
    binario_aux = np.array([])
    for i in range(nelementos - binario.size):
        binario_aux = np.concatenate(([0],[0]))
    binario =  np.concatenate((binario_aux, binario))
    return binario

#n = 4
#for i in range(n**n):
    #print( list_base_change(i, n, n) )
    #print(list_base_change_np(i, n, n))


#print(list_base_change_np(10, 2, 8))