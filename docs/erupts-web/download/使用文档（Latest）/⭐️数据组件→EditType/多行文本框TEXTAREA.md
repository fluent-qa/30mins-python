# 多行文本框 TEXTAREA 


## 使用方法
```java
@Lob  //定义数据库类为大文本类型，支持存入更多的数据
@EruptField(
    views = @View(title = "多行文本框"),
    edit = @Edit(title = "多行文本框", type = EditType.TEXTAREA)
)
private String textarea;
```

## 效果演示
![image.png](./img/-lQZ8-ZITZwGfow0/1611567527017-a7fccb70-7d05-458d-a522-b7353f0929f4-292077.png)


> 原文: <https://www.yuque.com/erupt/rug0gy>