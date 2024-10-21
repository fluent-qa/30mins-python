#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
 抛硬币示例：
抛硬币中奖的概率是1/2。但是，我们有没有办法从实验上证明这一点呢？
 在这个例子中，我们将使用蒙特卡罗方法迭代地模拟抛硬币5000次，
 以找出为什么头部或尾巴的概率总是1/2。如果我们重复抛硬币很多很多次，
 那么我们可以在概率值的准确答案上获得更高的精确度。
 在这个例子中，我们将使用Monte-Carlo方法反复模拟抛硬币5000次，
以找出头部或尾部的概率始终是1/2的概率。
"""
import random


import numpy as np
import matplotlib.pyplot as plt
def coin_flip()->int:
    """
    #0-> Heads
    #1-> Tails
    随机函数0，1
    :return:
    """
    return random.randint(0,1)

def coin_monte_carlo(n):
    results=0
    result_list =[]
    for i in range(n):
        flip_result = coin_flip()
        results = results+flip_result ## 计算出现正面总次数
        ## prob
        prob_value = results/(i+1)
        result_list.append(prob_value)
        plt.axhline(y=0.5,color='r',linestyle='-')
        plt.xlabel('次数')
        plt.ylabel('正面概率')
        plt.plot(result_list)
    return results/n
if __name__ == '__main__':

    print(coin_flip())
    answer = coin_monte_carlo(100)
    print(answer)

