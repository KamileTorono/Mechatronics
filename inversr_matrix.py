#!usr/bin/env python

#write a program to calculate the deteminant pf a matrix
""""
matrix_a = [[3,1],
            [4,2]]
det_a = (3*2) - (4*1)
print(det_a)
"""



#Calculater the inverse of a matrx

matrix_b = [[3,2],[6,4]]
det_b = (matrix_b[0][0] * matrix_b[1][1])- (matrix_b[0][1] *matrix_b[1][0])
print(det_b)

inv_b = [[0,0],[0,0]]
inv_b[0][0] = 1/det_b * matrix_b[1][1]
inv_b[0][1] = -1/det_b * matrix_b[0][1]
inv_b[1][0] = -1/det_b * matrix_b[1][0]
inv_b[0][0] = 1/det_b * matrix_b[0][0]

print(inv_b)
