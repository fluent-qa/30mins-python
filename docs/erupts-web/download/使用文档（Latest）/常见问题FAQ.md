#  🔭 常见问题 FAQ


## 启动项目未创建用户与菜单
初始化用户数据 erupt 只执行一次，使用 **.erupt** 文件夹进行标识，删除 **.erupt **文件夹，重启项目即可执行用户菜单插入sql


## 登录时密码加密规则
> 如果不希望登录时密码加密，在配置文件中，将：erupt-app.pwdTransferEncrypt 设置为 false 即可

```java
1.12.11 及以上版本
md5(md5(pwd) + account)


1.12.10 及以下版本
md5(md5(pwd)+ Calendar.DAY_OF_MONTH +account)
Calendar.DAY_OF_MONTH → Calendar.getInstance().get(Calendar.DAY_OF_MONTH) //今天月的哪一天
```


## 没有建表SQL
erupt 底层使用了 jpa 作为 ORM 数据层，可以在项目启动时完成自动建表的操作，所以不需要执行初始化 SQL 语句


## .erupt文件夹存放位置
标识文件位置为：${System.getProperty("user.dir")} / .erupt /

System.getProperty("user.dir")的值在不同环境会有差异，参照如下：

| 部署方式 | 目录位置 |
| --- | --- |
| jar | jar包同级目录 |
| Linux tomcat  | tomcat目录 |
| Windows tomcat | tomcat的bin目录 |

注：.erupt 文件夹是 '.'  开头的，该类型文件夹在操作系统中默认是隐藏的


## 一对多排序
添加 jpa 提供的 @OrderBy 注解
```java
@OneToMany(cascade = CascadeType.ALL)
@JoinColumn(name = "xxxx_id")
@OrderBy("field")
private Set<Test> test;
```


## 隐藏登录页面版权信息
详见 [app.js](https://www.yuque.com/erupts/erupt/gtp7iw#eqee9) copyright 配置


## 替换页签Logo
public 目录为 spring boot 规定的外部访问目录，在public目录下，创建 **favicon.ico** 文件即可
![image.png](./img/LA7XRoFHDbLmcrDJ/1610697786790-e7cb5101-847a-4cba-9836-130a445fc1be-429973.png)


## 使用UUID作为主键（优点：所有数据库通用，便于移植）
```java
@Id
@GeneratedValue(generator = "system-uuid")
@GenericGenerator(name = "system-uuid", strategy = "uuid")
@Column(name = "id", length = 32)
@EruptField
private String id;
```


## 一对多组件，添加多条数据仅有一条保存成功
**可能原因**：一对多情况使用Set集合存储，Set集合去重依赖于对象的HashCode方法，请检查多的一方是否使用了 **Lombok **的 **@Data **注解，该注解重写了 **HashCode** 方法，对set集合去重判断产生了影响

**解决办法**：使用**@Getter**注解与**@Setter**注解代替**@Data**注解



## Jar方式部署正常启动，Tomcat方式部署无法正常启动
请检查当前spring boot版本是否支持你使用的tomcat版本，例如：
**Spring boot 2.3.4.RELEASE **所支持的Tomcat版本为 **9.0.38**


## 表格查询效率低
可能原因：使用了lombok 的@data注解，该注解会重写toString方法，此举可能会导致复杂对象关系的数据在序列化时比较耗时，或者内存溢出，建议采用@Getter/@Setter注解



## BaseModel 与 HyperModel 的作用
BaseModel中定义了主键信息，添加了兼容各类数据库自增模式的注解，仅仅为兼容不同数据库而准备

HyperModel继承了BaseModel定义了创建时间、更新时间、创建人、更新人，只要继承HyperModel，erupt就可以帮助自动注入这几个字段的值，原理是HyperModel类上存在有 **@PreDataProxy(HyperDataProxy.class) **注解！



## 使用 new RuntimeException() 前端不提示错误信息
原因：SpringBoot 2.2和2.3异常处理的一个小变化，即RuntimeException错误堆栈信息需要开启配置才可抛出前端展示。解决办法：

- 新增了一个配置项server.error.includeMessage，默认是NEVER，因此默认是不是输出message的，只要开启就可以了。
- 使用throw new **EruptWebApiRuntimeException**("error info")抛出异常。
- 使用throw new **EruptApiErrorTip**("") 抛出异常（支持各类UI样式）


## 获取当前登录用户
```java
@Autowired  //注意：使用自动注入注解，需添加类bean注解,如：@Service、@Component
private EruptUserService eruptUserService;

public void test(){
	EruptUser eruptUser  = eruptUserService.getCurrentEruptUser()
}
```

## 多对一对象，存储id以外的列
使用@JoinColumn(referencedColumnName = "code")，标识code列存储到数据库中
```java
@ManyToOne
@JoinColumn(referencedColumnName = "code")
@EruptField(
    views = @View(title = "文章", column = "title"),
    edit = @Edit(title = "文章选择", type = EditType.REFERENCE_TABLE,
         referenceTableType = @ReferenceTableType(label = "title", id = "id"))
)
private Article article_abc_def3;
```



# 其他问题


## org.hibernate.LazyInitializationException: Failed to lazily initialize a collection of role
解决办法：开启 open-in-view 配置



## Cannot enter synchronized block because "xyz.erupt.core.util.AnnotationUtil.engine" is null
报错原因是 java 15 放弃了对 nashorn 的维护，解决办法：

- 使用 jdk 15 以下的版本
- 使用 1.6.6 及以上 erupt 版本


## 启动 Erupt 未生成菜单
erupt扩展库可能用到了jpa来自动生成数据库表与基础数据，请检查是否开启自动建表配置
**自动建表配置为：spring.jpa.generate-ddl = true**


## 启动 Erupt 前端无法正常解析数据，页面加载异常
erupt生成的接口返回参数被拦截，查看是否有统一的数据返回， 可将封装数据的范围缩小至包，不应该将所有应用了RestController注解类或方法都统一返回


## 菜单访问 Erupt 实体类后，启动提示404
请检查入口类中的 **@EruptScan **注解配置，包扫描路径是否包含你创建的实体类路径


## 一对多新增保存后，多的一方数据丢失
_在一对多的映射情况下，多的一方如果存有一的一方的对象，那么这个对象必须赋值否则会出现该问题_
_可通过 dataproxy → _beforeUpdate 进行对象填充


## 富文本编辑器图片上传成功，但不能回显
原因推测：erupt访问路径非根路径，如URL：[https://www.erupt.xyz/demo](https://erupt.xyz/demo/#/)，demo为根路径，导致ueditor找不到图片。
解决办法：配置虚拟目录映射
```nginx
# Nginx 虚拟目录配置
# 配置文件 /etc/nginx/nginx.conf
server {
  location /erupt-attachment/ {
    # alias值为你的图片存储路径
    alias /opt/attachment/;
    expires      30d;
  }
}
```
```xml
<!-- Tomcat 虚拟目录配置 -->
<!-- 在tomcat的conf目录的sever.xml文件的<Host></Host>标签中进行配置，格式如下 -->
<Host>
  <!--path属性必须为erupt-attachment  docBase按照实际附件存储路径填写 -->
  <Context path="/erupt-attachment" docBase="/opt/attachment" />
</Host>
```


## 一对多，多对一不创建外键关系
```java
@ManyToOne
@JoinColumn(foreignKey = @ForeignKey(ConstraintMode.NO_CONSTRAINT))
private Test test;
```

## 

## Erupt-magic-api生产环境https部署提示 404
调整 nginx 配置
![00c4e56df9345dcad48b17b898b16e84.png](./img/LA7XRoFHDbLmcrDJ/1710493499908-2ae951c1-41d1-471c-8c03-23132ace66ad-943351.png)

## 

## 更多问题
更多问题可访问如下链接，是热心网友帮助整理，欢迎查看点赞：
[https://www.yuque.com/erupts/guide/index](https://www.yuque.com/erupter/guide/index)


> 原文: <https://www.yuque.com/erupt/vr4md2>