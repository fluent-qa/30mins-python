# 横向分割线 DIVIDE


## 使用方法
```java
@Transient //由于该字段不需要持久化，所以使用该注解修饰
@EruptField(
    edit = @Edit(title = "分割线", type = EditType.DIVIDE)
)
private String divide;
```

## 效果演示
![image.png](./img/Eq3MiMWR_Q-I7b0K/1607262163784-f511febb-0cce-4fe9-a027-218fc0a7d2bd-190698.png)


> 原文: <https://www.yuque.com/erupt/hgsnga>