# 权限控制 @Power

> 控制erupt类能力，包括：新增、修改、删除、导入、导出等


## 使用方法
```java
@Erupt(
       name = "Erupt",
       power = @Power(add = true, delete = true, 
                      edit = true, query = true, 
                      importable = false, export = false)
)
public class EruptTest extends BaseModel {
	
}
```


## 配置项注解定义
```java
public @interface Power {
    boolean add() default true; //数据新增功能

    boolean delete() default true; //数据删除功能

    boolean edit() default true; //数据修改功能

    boolean query() default true; //输入查询功能

    boolean viewDetails() default true; //数据查看功能

    boolean export() default false; //数据导出功能

    boolean importable() default false; //数据导入功能

    //实现此接口动态控制权限
    Class<? extends PowerHandler> powerHandler() default PowerHandler.class;
}
```
```java
public interface PowerHandler {

    /**
     * 动态控制各功能使用权限
     * @param power 增删改查等功能的简单pojo对象
     */
    void handler(PowerObject power);

}
```
![image.png](./img/h8u6R6kENJdpaR3J/1609146105844-6541d8dc-0d64-4032-ace2-04957821af5a-817297.png)


> 原文: <https://www.yuque.com/erupt/wf4tbr>