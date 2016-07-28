import numpy as np
#生成矩阵

myZero = np.zeros([3,5]) # 3*5的全0矩阵
print myZero

print '-------------------------------'

myOne = np.ones([3,5]) #3*5的全1矩阵
print myOne

print '-------------------------------'

myRand = np.random.rand(3,4) #3行4列的0~1之间的随机数矩阵
print myRand

print '-------------------------------'

myEye = np.eye(3) # 3*3的单位矩阵
print myEye
