import numpy as np


def matrixmult (matrix1, matrix2): #Multiplies matrix1 x matrix2 (in that order)
    #First, i check if the dimensions are correct
    #if (matrix1.shape[1] != matrix2.shape[0]):  #BUG --> NOT ALL MATRIX ARE 2-DIMENSIONAL. SO IF ONE OF THE MATRICES IS 1-DIMENSIONAL, THE CODE BREAKS HERE!
    #    return 
    
    #Now, i do the multiplication
    result_matrix = np.zeros((matrix1.shape[0], matrix2.shape[1]))

    #elem --> is the i-th element of the new matrix
    elem = 0
    indexrowm1 = 0
    indexrowmresult = 0
    indexcolmresult = 0

    #Itera por las filas de la matriz1 y multiplica cada i-elemento con el i-elemento en la columna de la matriz2, luego suma ese 
    #producto y lo asigna como primer elemento en la matriz resultado
    for rowm1 in matrix1:
        for indexcolm2 in range(0, matrix2.shape[1]):
            for indexrowm2 in range(0, matrix2.shape[0]):
                elem += rowm1[indexrowm1] * matrix2[indexrowm2, indexcolm2]
                indexrowm1 += 1
            indexrowm1 = 0
            result_matrix[indexrowmresult, indexcolmresult] = elem
            indexcolmresult += 1
            elem = 0
        indexrowmresult += 1
        indexcolmresult = 0
    
    #Then, I finally return the matrix
    return result_matrix

def scalarMult (matrix, scalar): #Multiplies a matrix by a scalar
    indexrowmresult = 0
    indexcolmresult = 0

    result_matrix = np.zeros(matrix.shape)

    for row in matrix:
        for index in range(0, matrix.shape[1]):
            newelem = scalar * row[index]
            result_matrix[indexrowmresult, indexcolmresult] = newelem
            indexcolmresult += 1
        indexrowmresult += 1
        indexcolmresult = 0
    
    return result_matrix

def sumMatrix (matrix1, matrix2):
    indexrowmresult = 0
    indexcolmresult = 0
    
    result_matrix = np.zeros((matrix1.shape[0], matrix2.shape[1]))

    for rowindex in range(0, matrix1.shape[0]):
        for colindex in range(0, matrix1.shape[1]):
            newelem = matrix1[rowindex, colindex] + matrix2[rowindex,colindex]
            result_matrix[indexrowmresult, indexcolmresult] = newelem
            indexcolmresult += 1
        indexrowmresult += 1
        indexcolmresult = 0

    return result_matrix



    






