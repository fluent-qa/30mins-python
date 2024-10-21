# NoSQL数据源 erupt-mongodb


## 使用方法
1、在导入erupt的前提下，导入erupt-mongodb依赖
```xml
<dependency>
  <groupId>xyz.erupt</groupId>
  <artifactId>erupt-mongodb</artifactId>
  <version>${erupt.version}</version>
</dependency>
```
2、application.yml增加mongodb连接配置：
```yaml
spring:
	data:
    mongodb:
      uri: mongodb://user:secret@127.0.0.1/xxx
```
注：mysql的配置不能移除，需要用mysql存储基础数据

## 代码示例
与关系型数据库作为数据源时注解配置差别不大，要注意的是增加了@EruptDataProcessor与@Document注解！

图书管理系统为例：
```java
@EruptDataProcessor(EruptMongodbImpl.MONGODB_PROCESS)  //此注解表示使用MongoDB来处理数据
@Document(collection = "book") //把一个java类声明为mongodb的文档
@Erupt(
        name = "图书管理",
        orderBy = "sort"
)
public class Book {

    @Id
    @EruptField
    private String id;

    @EruptField(
            views = @View(title = "书名", sortable = true),
            edit = @Edit(title = "书名", search = @Search(vague = true))
    )
    private String name;

    @EruptField(
            views = @View(title = "价格", sortable = true),
            edit = @Edit(title = "价格", search = @Search(vague = true))
    )
    private Double price;

    @EruptField(
            views = @View(title = "状态", sortable = true),
            edit = @Edit(title = "状态",
                    boolType = @BoolType(trueText = "上架", falseText = "下架"),
                    search = @Search)
    )
    private Boolean status;

    @EruptField(
            views = @View(title = "进货日期", sortable = true),
            edit = @Edit(title = "进货日期", search = @Search(vague = true))
    )
    private Date date;

}
```



> 原文: <https://www.yuque.com/erupt/kf6ruk>