#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    newMatrix = matrix[:]
    for i in range(len(newMatrix)):
        newMatrix[i] = list(map(lambda x : x ** 2, newMatrix[i]))
    return (newMatrix)
