# 通用继承 @PreDataProxy

在erupt中可以通过继承，获取父类的组件的能力，也支持通过继承执行父组件预定义的方法，PreDataProxy定义如下：
```java
public @interface PreDataProxy {

    Class<? extends DataProxy<?>> value();

}
```

PreDataProxy 支持多级继承，也可以修饰在接口上


## 代码示例

继承 HyperModel 不仅可以使用创建人、创建时间、修改人、修改时间字段，还可以自动的将这些值注入，原理是 HyperModel 使用了 PreDataProxy 注解 ！
```java
@PreDataProxy(HyperDataProxy.class)
@MappedSuperclass //作用 jpa 父类标识注解
public class MetaModelVo extends BaseModel {

    @EruptField(
            views = @View(title = "创建人", width = "100px"),
            edit = @Edit(title = "创建人", readonly = @Readonly)
    )
    @EruptSmartSkipSerialize //作用：让子类也可定义同名字段，提升字段复用性
    private String createBy;

    @EruptField(
            views = @View(title = "创建时间", sortable = true),
            edit = @Edit(title = "创建时间", readonly = @Readonly, dateType = @DateType(type = DateType.Type.DATE_TIME))
    )
    @EruptSmartSkipSerialize
    private LocalDateTime createTime;

    @EruptField(
            views = @View(title = "更新人", width = "100px"),
            edit = @Edit(title = "更新人", readonly = @Readonly)
    )
    @EruptSmartSkipSerialize
    private String updateBy;

    @EruptField(
            views = @View(title = "更新时间", sortable = true),
            edit = @Edit(title = "更新时间", readonly = @Readonly, dateType = @DateType(type = DateType.Type.DATE_TIME))
    )
    @EruptSmartSkipSerialize
    private LocalDateTime updateTime;
}
```
```java
@Service
public class HyperDataProxy implements DataProxy<HyperModel> {

    @Autowired
    private EruptUserService eruptUserService;

    @Override
    public void beforeAdd(HyperModel hyperModel) {
        hyperModel.setCreateTime(new Date());
        hyperModel.setCreateUser(new EruptUser(eruptUserService.getCurrentUid()));
    }

    @Override
    public void beforeUpdate(HyperModel hyperModel) {
        hyperModel.setUpdateTime(new Date());
        hyperModel.setUpdateUser(new EruptUser(eruptUserService.getCurrentUid()));
    }
}
```


> 原文: <https://www.yuque.com/erupt/nruzv8>