# 数字滑块 SLIDER

滑动型输入器，展示当前值和可选范围


## 使用方法
```java
@EruptField(
    edit = @Edit(title = "数字滑块", 
                 type = EditType.SLIDER, 
                 sliderType = @SliderType(max = 100))
)
private Integer slider;
```



## 配置项注解定义
```java
public @interface SliderType {
    int max();  //滑块最大值

    int min() default 0;  //滑块最小值

    int step() default 1; //步进

    boolean dots() default false;  //是否只能拖拽到刻度上

    int[] markPoints() default {}; //刻度数组
}
```

## 代码演示

#### 指定可选刻度
```java
@EruptField(
    edit = @Edit(title = "栅格数", 
                 type = EditType.SLIDER,
                 sliderType = @SliderType(max = 12, markPoints = {1, 2, 3, 4, 6, 8, 12}, dots = true))
)
private Integer grid = 1;
```


## 效果演示
![image.png](./img/9NGEfTMRmOjHT15l/1611567947322-52af2a69-429b-4f56-b488-60a5f30c44c0-919108.png)


> 原文: <https://www.yuque.com/erupt/as6vhc>