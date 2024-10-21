# Python 生成均值为2 ，标准差为3 的一维正态分布样本500

import math
# std_dev= uncertainty/sqrt(n)
# 根据数值A及其不确定性x%（均值为A，标准差“西格玛的平方”为 x%*A/2  ），按照正态分布的频率取一百万个数值；
import numpy as np

mean = 10
uncertainty = 2
n = 1000000000

std_dev = uncertainty / math.sqrt(n)

print("标准差为:", std_dev)

arr = [1, 2, 3, 4, 5, 6, 100, 90]
print(np.var(arr))
print(math.sqrt(np.var(arr,ddof=1)))
print(np.mean(arr))
print(np.std(arr,ddof=1))
print(np.std(arr,ddof=1)/math.sqrt(len(arr)))
