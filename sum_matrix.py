# coding:utf-8
from numpy import *

myOne = ones([3 , 3])
myEye = eye(3)
print myOne+myEye  # 矩阵的加法
print '----------------------------'
print myOne-myEye  # 矩阵的减法
print '----------------------------'
mymatrix = mat( [[1,2,3],[4,5,6],[7,8,9]] )
a = 10
print a*mymatrix #一个数乘以一个矩阵
print '----------------------------'
print sum(mymatrix) #计算矩阵所有元素和
print '----------------------------'
mymatrix2 = 1.5*ones([3,3]) #矩阵乘以矩阵
print multiply(mymatrix,mymatrix2)
print '----------------------------'
print power(mymatrix , 2)  # 矩阵各元素的n次方
print '----------------------------'
mymatrix3 = mat([[1],[2],[3]])
print mymatrix*mymatrix3 #两个矩阵相乘
print '----------------------------'
print mymatrix.T #矩阵的转置
mymatrix.transpose()
print mymatrix
