# Pytest 顺序执行，依赖执行，参数化执行

进行下面实验前，需要安装python和pytest，我一般用poetry来管理,如何创建就是以下几个命令:

```shell
poetry init 
poetry add pytest --group test
```

<!-- TOC -->

* [Pytest 顺序执行，依赖执行，参数化执行](#pytest-顺序执行依赖执行参数化执行)
    * [0- 被测对象](#0--被测对象)
    * [1. 使用pytest进行测试这个服务的常见场景和解法](#1-使用pytest进行测试这个服务的常见场景和解法)
    * [1.1 pytest-单独测试一个方法](#11-pytest-单独测试一个方法)
    * [1.2 Pytest-测试方法B但是需要先执行测试方法A](#12-pytest-测试方法b但是需要先执行测试方法a)
    * [1.3 pytest - 参数化执行](#13-pytest---参数化执行)
    * [2. 使用的一些小结](#2-使用的一些小结)

<!-- TOC -->

## 0- 被测对象

假设被测试对象就是一个计算加减乘除的一个服务，这里把一个方法就等同于一个API接口，实际上也确实没有
太大区别，一个是本地调用，一个是远程调用，远程调用需要一个客户端，本地调用直接就用这个类调用了

```python
"""
service functions for calculation
"""


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a * 1.0 / b
```

## 1. 使用pytest进行测试这个服务的常见场景和解法

1. 单独测试一个方法
2. 测试方法B但是需要先执行测试方法A
3. 参数化测试，参数可能是静态写死的，也可能是动态的

## 1.1 pytest-单独测试一个方法

使用如下方法就可以进行单独的方法测试，基本原则就是： ***一个方法一个测试，测试数据都固定***

```python
import allure
import pytest

from app.module_a.service import subtract, add


@allure.feature("减法结果为正")
def test_subtract_positive():
    result = subtract(2, 1)
    assert result == 1


@allure.feature("减法结果为为负数")
def test_subtract_negative():
    result = subtract(1, 2)
    assert result == -1

```

## 1.2 Pytest-测试方法B但是需要先执行测试方法A

如果遇到： 测试方法B但是需要先执行测试方法A，这里面有一些小问题就是：

1. 顺序不能绝对保证: 如果通过运行pytest的命令行时候，有可能不能***确保测试A一定跑在测试B前面***
2. 测试可读性问题: s不仔细看代码，不能看出来-测试方法B但是需要先执行测试方法A

这个问题可以通过pytest的插件 pytest-order 来解决:

```shell
poetry add pytest-order
```

测试代码如下: 通过@pytest.mark.order定于显示的定于运行顺序，好处有两个：

1. 确保顺序
2. 提高测试可读性，一眼就看出来那个先跑那个后跑
3. 不好的地方是： 单独运行第二个测试： test_subtract_order 会报错，但是因为写了order标识，
   大概一下子也能明白怎么回事

```python
context = {}


@pytest.mark.order(1)
def test_add_positive():
    result = add(1, 2)
    assert result == 3
    context['USED_FOR_SUBTRACT'] = result


@allure.feature("被减数是加法函数计算出来的结果")
@pytest.mark.order(2)
def test_subtract_order():
    result = subtract(1, context['USED_FOR_SUBTRACT'])
    assert result == -2

```

如果使用pytest-dependency插件解决，代码也类似,就不多说明了：

```python
context = {}


@pytest.mark.order(1)
@pytest.mark.dependency()
def test_add_positive():
    result = add(1, 2)
    assert result == 3
    context['USED_FOR_SUBTRACT'] = result


@pytest.mark.dependency(depends=["test_add_positive"])
def test_subtract_dep():
    result = subtract(1, context['USED_FOR_SUBTRACT'])
    assert result == -2
```

这里面注意一点： 用来存数据的用字典会好那么一点，为了避免一些想不到的麻烦我自己就一直用字典了，也没有用global这样的东西。

## 1.3 pytest - 参数化执行

- 有时很多case都很类似，只要给数据自动跑就行了，不想写很多单独的测试方法了，就用参数化执行，
  最简单的就是直接给上固定的数据, 以下代码一看就明白

```python
fixed_params = [(1, 2, 3), (-1, 1, 0)]


@pytest.mark.parametrize('a,b,expected', fixed_params)
def test_add_parameterized(a, b, expected):
    actual = add(a, b)
    assert actual == expected
```

- 有时呢，参数化的时候有一两个数字是需要动态获得以下的，那么可以用以下方式简单处理以下,
  就是写一个函数区构建这些参数化的测试数据

```python
def dynamic_cases():
    d_params = [(1, 2, 3), (-1, 1, 0)]
    dynamic_case = (1, add(1, 2), 4)
    d_params.append(dynamic_case)
    return d_params


@pytest.mark.parametrize('a,b,expected', dynamic_cases())
def test_add_parameterized(a, b, expected):
    actual = add(a, b)
    assert actual == expected
```

## 2. 使用的一些小结

有时可能更复杂，那么其实呢，我自己的做法就是：

1. 混合使用顺序order/依赖空dependency和参数化化进行处理
2. 能参数化的和复杂的case分开，比如:
   A. 一些异常错误数据，出错信息的测试，这些参数化可能容易一些就参数化了
   B. 复杂场景的，计算，拿前一个返回再构建后一个的人参之类的，***干脆就单独写一个测试方法了***
3. 不去想一个统一的解法，写代码和在测试平台上写测试用例的最大的区别就是：***测试平台一般想用一种方法解决所有问题***，
   而自己写代码的坏，就是***完全自己控制灵活度***， 各有好坏，既然自己写代码了，
   那就多多利用写代码的灵活度解决自己的问题，有时找一个可以适用所有的方法可能很麻烦，不如直接手写一个测试方法来的简单直接
   还节约一点时间。





