# 评分器 RATE

注：1.12.0及以上版本支持

### 注解示例
```java
@EruptField(
        edit = @Edit(
            	title = "评分", 
            	type = EditType.RATE,
                rateType = @RateType(allowHalf = true, count = 10)
        )
)
private Float rate;
```

### 效果展示
![image.png](./img/_thLyAs_byoES4DQ/1688309356376-3677f142-034e-47e5-a429-802a21b16527-822905.png)

### rateType注解定义
```java
public @interface RateType {

    //自定义字符
    String character() default "";

    //是否允许半选，如果为 true 字段类型必须用浮点类型修饰
    boolean allowHalf() default false;

    //star 总数
    int count() default 5;

}
```


> 原文: <https://www.yuque.com/erupt/cp8bu0vttekg495o>