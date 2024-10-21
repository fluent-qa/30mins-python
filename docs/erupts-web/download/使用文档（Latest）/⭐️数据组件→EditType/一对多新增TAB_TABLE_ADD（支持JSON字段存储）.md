# 一对多新增 TAB_TABLE_ADD （支持 JSON 字段存储）


## 使用方法
```java
// 注：orphanRemoval 配置在 1.6.4 版本以后开始支持
@OneToMany(cascade = CascadeType.ALL, orphanRemoval = true) //一对多，且开启级联
@JoinColumn(name = "this_id") //this表示当前的表名，如：order_id子表会自动创建该列来标识与主表的关系
@OrderBy //排序
@EruptField(
    edit = @Edit(title = "添加多条表格数据", type = EditType.TAB_TABLE_ADD)
)
private Set<Table> tables; //Table对象定义如下👇
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

## 效果演示
![image.png](./img/Kf5n3i011liu9kUg/1611566038179-e28d5de4-4d30-4493-8ca5-69e9ab76fd3c-981382.png)
![image.png](./img/Kf5n3i011liu9kUg/1611566090789-ada19db5-9ca8-4a15-b430-c06a3b971f0c-677753.png)


## 一对多内容存储到 JSON 字段

1. 添加依赖
```xml
<dependency>
    <groupId>com.vladmihalcea</groupId>
    <artifactId>hibernate-types-52</artifactId>
    <version>2.21.1</version>
</dependency>
```

2. 增加类注解：@TypeDef，增加字段注解@Type@Column
```csharp
@Entity
@Table(name = "many_json")
@Erupt(name = "一对多内容存储到 JSON 字段")
@TypeDef(name = "json", typeClass = JsonStringType.class)
public class ManyJson extends BaseModel {

    @Type(type = "json")
    @Column(columnDefinition = "json" )
    @EruptField(
            edit = @Edit(
                    title = "json",
                    type = EditType.TAB_TABLE_ADD
            )
    )
    private Set<Table> tables; //Table对象定义参考上面
}

```

3. 入库效果

![image.png](./img/Kf5n3i011liu9kUg/1713965340236-d716b67b-a2dc-43c6-bfd7-1ae2c18f4612-149924.png)


> 原文: <https://www.yuque.com/erupt/uufoth>