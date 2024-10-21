# 排序 OrderBy

> 使用方式：
> 类名.字段名 [asc|desc]
> 多字段排序：类名.字段名 [asc|desc], 类名.字段名 [asc|desc] ...

```java
@Erupt(
       name = "Erupt",
       orderBy = "EruptTest.no desc"
)
public class EruptTest extends BaseModel {
    
    @EruptField(
            views = @View(title = "编号"),
            edit = @Edit(title = "编号")
    )
    private Integer no;
	
}
```


> 原文: <https://www.yuque.com/erupt/pbrolx>