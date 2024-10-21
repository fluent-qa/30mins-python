# 智能报表 erupt-bi

**未开源，bi 为 erupt 体系唯一付费模块，如需购买请联系作者**
![31701346746_.pic.jpg](./img/Gnl9rIXFAqXzA0AF/1701346757727-d67a80ab-41d7-48e8-af97-44feec484ce4-281735.jpeg)


### 模块介绍
数据分析相关功能，支持纯sql定义报表图表等功能，支持十几种查询维度，十几种图表组件，动态函数等能力
erupt-bi 本质上为数据库中间件协调与调度程序，几乎不占用资源，性能取决于已配置的SQL语句查询速度


![1716391469782-565a3a07-feb2-4d2e-ae2d-1f7528ecabbb.jpeg](./img/Gnl9rIXFAqXzA0AF/1716391469782-565a3a07-feb2-4d2e-ae2d-1f7528ecabbb-447756.jpeg)


### 演示地址
[https://www.erupt.xyz/demo](https://www.erupt.xyz/demo)
账号：bi
密码：bi
![image.png](./img/Gnl9rIXFAqXzA0AF/1671418652346-07f3de41-3ed3-47b3-870f-c5746c6a38e2-611288.png)
![image.png](./img/Gnl9rIXFAqXzA0AF/1671418719525-4d163a2f-3ef0-4c2f-a659-079d60addbf6-586096.png)
![image.png](./img/Gnl9rIXFAqXzA0AF/1671418759528-a0b2bbdf-dc63-492b-b737-58d04a0e5cf6-473913.png)
![1607265329568-406961c7-9c88-4155-b01b-d8a380f32081.png](./img/Gnl9rIXFAqXzA0AF/1607265329568-406961c7-9c88-4155-b01b-d8a380f32081-135681.png)


### 菜单配置项说明
| 菜单名称 | 功能说明 |
| --- | --- |
| 数据源管理 | 多数据源配置，需配置数据源的用户名密码等信息，特殊的数据源需要指定分页语句 |
| 报表处理类 | 需实现xyz.erupt.bi.fun.EruptBiHandler接口，可实现对报表sql的动态修改与查询结果的动态处理。 |
| 函数管理 | 配置函数脚本，用于报表中调用，提供了动态 SQL 的能力，有 and , like , In 等基础函数 |
| 参照维度 | 统一维护下拉列表下拉树等组件数据 |
| 报表配置 | 配置报表、图表、查询维度、动态列、缓存、分页、历史记录、菜单发布等 |






> 原文: <https://www.yuque.com/erupt/hstvzf>