# 🔝 Linq.J 对象查询语言

> Linq.J 是一个基于 Linq（C# 中的一个功能强大的查询 API）理念的 Java 库。它提供了与 LINQ 类似的查询语法，让你可以轻松地对数组和对象进行：查询、关联、排序、筛选、分组、分页等操作。


---

**Linq 是面向对象的 sql，linq实际上是对内存中数据的查询，使开发人员能够更容易地编写查询。这些查询表达式看起来很像 SQL，写法和 Spark SQL 类似**

| **开源地址，使用 MIT 协议无任何使用限制** |  |
| --- | --- |
| Gitee | GitHub |
| [YuePeng/Linq.J](https://gitee.com/erupt/linq) | [GitHub - erupts/Linq.J: Linq.J - LINQ for Java, Object Query Language (LINQ) library based on the JVM → Lambda feature](https://github.com/erupts/Linq.J) |


## 语法比较

### C# LINQ
```csharp
var user1 = new User() {UserId = "1", UserName = "张三", UserPhone = "1234567997"};
var user2 = new User() {UserId = "2", UserName = "李四", UserPhone = "18335789789"};
var users = new List<User>() { user1, user2 };

var whereQuery = from user in users where user.UserId == "1" select user;

var groups = from user in users
             group user by user.name into g select new {
                g.name,
                minAge = g.Min(p => p.age)
             }
```

### Spark SQL
```scala
val df = spark.read.json("E://people.json")
//输出DataFrame的内容
df.select($"name", $"age").filter($"age" > 21)

// 按照age分组，统计每种age的个数
df.groupBy("age").count().show()
// +----+-----+
// | age|count|
// +----+-----+
// |  19|    1|
// |null|    1|
// |  30|    1|
// +----+-----+
```

### Linq.J
```java
val people = file.json("E://people.json")
var names = Linq.from(people).select(People::getName).write(String.class);

Linq.from(people).between(People::getAge, 1, 3);

Linq.from(people).groupBy(People::getName)
            .select(
                Columns.of(TestSource::getName),
                Columns.min(TestSource::getAge, "min")
            )
```

## 应用场景示例
```csharp
/**
 * 你的数据库存储了学生的手机号身份证号等基本信息，另外一个系统存储了学生的留学信息，
 * 需要身份证做关联，并对外实时显示学生的留学情况
 */
public class demo {

    List<Student> students = db.query("select * from t_student");

    List<StudyAbroad> studyAbroads = http.get("https://www.yuque.com/erupts/xxx.do?identity =xx,xxx,xxxx,xx");

    //常规写法
    public void routine() {
        Map<String, StudyAbroad> studyAbroadMap =new HashMap<>();
        for (StudyAbroad studyAbroad : studyAbroads) {
            studyAbroadMap.put(studyAbroad.getIdentity(), studyAbroad);
        }
        for (Student student : students) {
            StudyAbroad studyAbroad = studyAbroadMap.get(student.getIdentity());
            if (null != studyAbroad){
                //留学时间
                student.setStudyAbroadTime(studyAbroad.getTime());
                //留学国家
                student.setStudyAbroadCountry(studyAbroad.getCountry());
            }
        }
    }

    //Linq.J写法
    public void linqJ() {
        List<Student> result = Linq.from(students)
                .leftJoin(studyAbroads, StudyAbroad::getIdentity, Student::getIdentity)
                .select(Student.class)
                .selectAs(studyAbroad::getTime, Student::getStudyAbroadTime)
                .selectAs(studyAbroad::getCountry, Student::getStudyAbroadCountry)
                .write(Student.class);
    }
    
}


```

| **更多语法和使用信息可到开源页查看 👇👇👇，使用 MIT 协议无任何使用限制** |  |
| --- | --- |
| GitHub | Gitee |
| [GitHub - erupts/Linq.J: Linq.J - LINQ for Java, Object Query Language (LINQ) library based on the JVM → Lambda feature](https://github.com/erupts/Linq.J) | [YuePeng/Linq.J](https://gitee.com/erupt/linq) |


## 



> 原文: <https://www.yuque.com/erupt/fl0lyrdlrbm9mg0g>