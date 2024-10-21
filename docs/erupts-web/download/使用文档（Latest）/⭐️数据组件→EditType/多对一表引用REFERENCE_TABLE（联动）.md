# 多对一表引用 REFERENCE_TABLE（联动）


## 使用方法
```java
@ManyToOne //多对一
@JoinColumn(name = "table")
@EruptField(
    views = {
        @View(title = "顺序", column = "sort"),
        @View(title = "名称", column = "name")
    },
    edit = @Edit(title = "多对一表格", type = EditType.REFERENCE_TABLE,
    	referenceTableType = @ReferenceTableType(id = "id", label = "name")
    )
)
private Table table; //Table对象定义如下👇
```
```java
@Entity
@Table(name = "TABLE")
@Erupt(name = "表格")
public class Table extends BaseModel {
    
    @EruptField(
            views = @View(title = "顺序"),
            edit = @Edit(title = "顺序")
    )
    private Integer sort;

    @EruptField(
            views = @View(title = "名称"),
            edit = @Edit(title = "名称")
    )
    private String name;
    
}
```

## 配置项注解定义
```java
public @interface ReferenceTableType {
    String id() default "id"; //多对一表中做存储的列

    String label() default "name"; //多对一表中做展示的列

    String dependField() default ""; //使根据依赖字段的值做匹配

    //获取dependField所指定字段的值与id列做匹配，获取匹配结果，如：dependField的值 = id
    String dependColumn() default "id";
}

```
![2021-01-25 17.25.44.gif](./img/_-BW4Y98wWtCEP2l/1611566861630-6d0460f6-cdb5-4573-950f-b75b47ca25b1-755366.gif)



> 原文: <https://www.yuque.com/erupt/xa4akx>