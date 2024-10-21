# 自定义登录逻辑 @EruptLogin


覆盖默认登录逻辑，可使用此功能对接LDAP、单点登录等能力


### 使用方法
在Spring Boot入口类中增加 **EruptLogin** 注解，注解值为 LoginProxy 接口的实现类
```java
@EruptLogin(TestLoginProxy.class)
@SpringBootApplication
@EntityScan
@EruptScan
public class EruptDemoApplication {

    public static void main(String[] args) {
        SpringApplication.run(EruptDemoApplication.class, args);
    }

}
```

### EruptLogin 注解定义
```java
// 仅需实现 LoginProxy 接口就可以自定义登录规则
public @interface EruptLogin {

    Class<? extends LoginProxy> value();

}
```

### LoginProxy 接口定义 
```java
public interface LoginProxy {

    @Comment("登录校验，如要提示校验结果请抛异常")
    @Comment("为安全考虑pwd是加密的，加密逻辑：md5(md5(pwd)+ Calendar.DAY_OF_MONTH +account)")
    @Comment("Calendar.DAY_OF_MONTH → Calendar.getInstance().get(Calendar.DAY_OF_MONTH) //今天是月的哪一天")
    @Comment("如果不希望加密，请前往配置文件，将：erupt-app.pwdTransferEncrypt 设置为 false 即可")
    EruptUser login(String account, String pwd);

    @Comment("登录成功")
    default void loginSuccess(EruptUser eruptUser, String token) {
    }

    @Comment("注销事件")
    default void logout(String token) {

    }

    @Comment("修改密码")
    default void beforeChangePwd(EruptUser eruptUser, String newPwd) {

    }

}

```


### 方法示例
```java
@Service //使用此注解实现依赖注入相关功能（可选）
public class TestLoginProxy implements LoginProxy {

    @Resource
    private EruptDao eruptDao;

    @Autowired
    private EruptUserService eruptUserService;
    
    // 额外请求参数可从 request 对象中获取
    @Resource
    private HttpServletRequest request;

    @Override
    public EruptUser login(String account, String pwd) {
        // 调用默认登录方法
        // eruptUserService.login(account, pwd);        
        // 错误提示
        // throw new RuntimeException("账号或密码错误"); 
        return eruptDao.queryEntity(EruptUser.class, "account = 'bi'"); //获取用户对象
    }

    @Override
    public void loginSuccess(EruptUser eruptUser, String token) {
        // TODO
    }

    @Override
    public void logout(String token) {
        // TODO
    }

	@Override
    public void beforeChangePwd(EruptUser eruptUser, String newPwd) {
     	// TODO   
    }
    
}

```

### 登录接口
```http
http://localhost:8080/erupt-api/login?account=xxx&pwd=xxxx

account:用户名
pwd:密码
```


> 原文: <https://www.yuque.com/erupt/cgg9af>