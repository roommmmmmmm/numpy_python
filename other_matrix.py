#coding:utf-8
from numpy import *

mymatrix = mat( [[1,2,3],[4,5,6],[7,8,9]] )
[m,n] = shape(mymatrix) #矩阵的行列数
print '矩阵的行数是 ：',m,'列数是 ：',n

myscll = mymatrix[0]
print '按行切片 :',myscll

myscll2 = mymatrix.T[0]
print '按列切片: ',myscll2

mycpmat = mymatrix.copy()
print '复制矩阵 : \n',mycpmat

print '矩阵元素的比较: \n',mymatrix < mymatrix.T
