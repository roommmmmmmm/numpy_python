# coding:utf-8
from numpy import *
# n阶方阵的行列式运算

A = mat( [[1,2,4,5,7,],[9,12,11,8,2,],[6,4,3,2,1,],[9,1,3,4,5,],[0,2,3,4,1]] )
print 'det(A): ',linalg.det(A); # 矩阵的行列式

invA = linalg.inv(A) # 矩阵的逆
print 'inv(A): \n',invA

AT = A.T # 矩阵的对称
print '对阵矩阵为:\n',A*AT

print '矩阵的秩为:',linalg.matrix_rank(A) # 矩阵的秩
