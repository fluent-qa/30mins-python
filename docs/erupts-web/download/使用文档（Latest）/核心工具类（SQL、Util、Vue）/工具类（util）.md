# 🦊 工具类（util）

**erupt 开发常用工具类整理**


## 获取登录用户上下文信息
> 可以在 dataProxy 等场景中获取，如果自定义接口需要传递 Token

```java
@Component
public class Test{
    
    @Autowired
    private EruptUserService eruptUserService;
    
    @Autowired
    private EruptContextService eruptContextService;

    public void test(){

        // 获取当前登录用户ID
        Long uid = eruptUserService.getCurrentUid();

        // 获取当前登录用户对象（eruptUser）
        EruptUser eruptUser = eruptUserService.getCurrentEruptUser();
        
        // 获取当前用户基础信息（不查数据库）
        AdminUserinfo adminUserinfo = eruptUserService.getAdminUserInfo();

        // 获取当前请求token
        String token = eruptContextService.getCurrentToken();

        // 获取当前访问菜单
        EruptMenu eruptMenu = eruptContextService.getCurrentEruptMenu();

        // 获取erupt上下文类对象
        // 获取的是有Erupt注解的类
        Class<?> clazz = eruptContextService.getContextEruptClass();

    }
}
```

## 

## 继承实体类达到某些能力
```java
@Erupt(name = "只显示当前用户录入的数据")
public class EruptClass extends LookerSelf {
	//TODO 字段定义
}

@Erupt(name = "自动管理创建人，创建时间，更新人，更新时间字段")
public class EruptClass extends HyperModel {
	//TODO 字段定义
}
```
| 可继承类名称 | 功能说明 |
| --- | --- |
| BaseModel | 管理数据库主键，通用性配置，支持所有主流数据库 |
| 数据审计（外键关联） |  |
| HyperModel | 自动管理创建人，创建时间，更新人，更新时间字段 |
| HyperModelVo | 自动管理创建人，创建时间，更新人，更新时间字段，且在页面中展示这些数据 |
| HyperModelCreatorVo | 自动管理创建人，创建时间，更新人，更新时间字段，且展示创建人与创建时间 |
| HyperModelUpdateVo | 自动管理创建人，创建时间，更新人，更新时间字段，且展示更新人与更新时间 |
| 数据审计（非外键关联，不关联用户表，保存当前用户名） |  |
| MetaModel | 自动管理创建人，创建时间，更新人，更新时间字段（不关联用户表） |
| MetaModelVo | 自动管理创建人，创建时间，更新人，更新时间字段，且在页面中展示这些数据（不关联用户表） |
| MetaModelCreateVo | 自动管理创建人，创建时间，更新人，更新时间字段，且展示创建人与创建时间（不关联用户表） |
| MetaModelUpdateVo | 自动管理创建人，创建时间，更新人，更新时间字段，且展示修改人与修改时间（不关联用户表） |
| 权限过滤> 不支持多层嵌套使用，如果类嵌套层级过深，建议模仿 LookerXXX 写法，自定义权限过滤类

 |  |
| LookerSelf | 只显示当前用户录入的数据      **（**管理员登录可看所有数据**）** |
| LookerOrg | 只显示当前用户所属组织的数据**（**管理员登录可看所有数据**）** |
| LookerPostLevel | 显示当前组织内，职位权重低于登录用户的数据**（**管理员登录可看所有数据**）** |
| 如果有其他自定义需求，可以通过[@PreDataProxy](https://www.yuque.com/erupts/erupt/nruzv8)自由定义 |  |



## 使用 Erupt 类完成JDBC操作
> Student是一个被erupt可视化的实体类，如果想在业务中查询Student数据可以采用如下方法

[🔍 使用 EruptDao 与数据库交互](https://www.yuque.com/erupts/erupt/wgc30d?view=doc_embed&inner=mxI1r)
```java
@Service
public class EruptJdbc {
    
    @Resource
    private EruptDao eruptDao;

    //通用对象查询
    public void lambdaQuery() {
        List<EruptUser> eruptUser2 = eruptDao.lambdaQuery(EruptUser.class)
                .like(EruptUser::getName, "e")
                .isNull(EruptUser::getWhiteIp)
                .in(EruptUser::getId, 1, 2, 3, 4)
                .ge(EruptUser::getCreateTime, "2023-01-01")
                .addCondition("whiteIp is null")
                .isNotNull(EruptUser::getCreateTime)
                .offset(1).limit(2)
                .orderBy(EruptUser::getCreateTime)
                .orderByDesc(EruptUser::getCreateTime)
                .list();
    }

    //原生sql查询
    public void navtiveQuery(Goods goods){
        List<Map<String, Object>> list = eruptDao.getJdbcTemplate()
            .queryForList("select * from t_table");
    }

    //新增
    public void add(Student student){
        eruptDao.persist(student);
        // 使用 flush 方法可以在线程结束前入库，如果批处理数据建议每千次（新增、更新、删除）调用一次 flush
        eruptDao.flush();
    }

    //修改
    public void modify(Student student){
        eruptDao.merge(student);
    }

    //删除
    public void delete(Student student){
        eruptDao.delete(student);
    }
   
}
```


## 错误消息提示 & 对话框通知
> 在任意方法中抛出该异常即可达到对应效果

```java
public void fun(){
    //对话框方式提示
    throw new EruptApiErrorTip("错误信息提示")

    //消息方式提示
    throw new EruptApiErrorTip("错误信息提示",EruptApiModel.PromptWay.MESSAGE)
        
    //通知方式提示
    throw new EruptApiErrorTip("错误信息提示",EruptApiModel.PromptWay.NOTIFY)
}
```

## 


## 登录密码加密传输规则
[ 🔭 常见问题 FAQ](https://www.yuque.com/erupts/erupt/vr4md2?view=doc_embed&inner=jgebi)


> 原文: <https://www.yuque.com/erupt/plk783>