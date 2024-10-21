# 布尔开关 BOOLEAN

**布尔开关选择**


## 使用方法
如果字段类型为Boolean可自动推测出组件类型type为BOOLEAN
```java
@EruptField(
    edit = @Edit(
        title = "布尔选择器",
        boolType = @BoolType
    )
)
private Boolean bool;


@EruptField(
    edit = @Edit(
        title = "设定默认选中值",
        boolType = @BoolType
    )
)
private Boolean bool2 = true;
```

## 配置项注解定义
```java
public @interface BoolType {
    
    String trueText() default "是";   //选中时文本

    String falseText() default "否";  //非选中时文本

    
    ////默认选中状态，该配置在1.6.7版本以后废弃，请使用给字段赋值的方式代替此功能
    boolean defaultValue() default true; 

}
```


## 代码演示
```java
@EruptField(
    edit = @Edit(title = "任务状态", 
                 boolType = @BoolType(trueText = "成功", falseText = "失败"))
)
private Boolean status;
```


## 效果演示
![image.png](./img/oBVYYtYoQxwI5bPB/1620454424937-afced029-50fc-49c0-94d6-d50bde826442-776065.png)


> 原文: <https://www.yuque.com/erupt/afkbtm>