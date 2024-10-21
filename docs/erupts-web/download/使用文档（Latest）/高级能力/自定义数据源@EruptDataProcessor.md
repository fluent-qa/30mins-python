# 自定义数据源 @EruptDataProcessor

如果你希望用 erupt 管理数据库以外的数据可以使用自定义数据源的方式实现


## 使用场景

- 外部API接口的的显示与处理（Http、Dubbo）
- CSV、TSV 等数据文件的可视化管理
- 对接其他外部数据源，如 ES、MongoDB


## 使用方法

1、实现 IEruptDataService 接口
```java
public interface IEruptDataService {

    /**
     * 全局控制数据源内功能操作能力 1.12.12及以上版本支持
     * 比如当前数据源实现无删除和新增能力，在此控制即可，无需在@Erupt → @Power 处再次声明
     *
     * @return 页面能力控制
     */
    default PowerObject power() {
        return new PowerObject();
    }

    /**
     * 根据主键id获取数据
     *
     * @param eruptModel erupt核心对象
     * @param id         id
     * @return 通过id获取到的数据
     */
    Object findDataById(EruptModel eruptModel, Object id);

    /**
     * 查询分页数据
     *
     * @param eruptModel erupt核心对象
     * @param page       page 分页参数
     * @param query      查询对象
     * @return 页面对象
     */
    Page queryList(EruptModel eruptModel, Page page, EruptQuery eruptQuery);

    /**
     * 根据列查询相关数据
     *
     * @param eruptModel eruptModel
     * @param columns    列
     * @param query      查询对象
     */
    Collection<Map<String, Object>> queryColumn(EruptModel eruptModel, List<Column> columns, EruptQuery eruptQuery);


    /**
     * 添加数据
     *
     * @param eruptModel erupt核心对象
     * @param object
     */
    void addData(EruptModel eruptModel, Object object);

    /**
     * 修改数据
     *
     * @param eruptModel erupt核心对象
     * @param object     数据对象
     */
    void editData(EruptModel eruptModel, Object object);

    /**
     * 删除数据
     *
     * @param eruptModel erupt核心对象
     * @param object     数据对象
     */
    void deleteData(EruptModel eruptModel, Object object);

}
```
2、注册自定义数据源
```java
//可以在static方法块或spring生命周期函数中注册
DataProcessorManager.register("数据源名称", EruptDataServiceImpl.class);
```
3、在 erupt 类上添加 EruptDataProcessor 注解
```java
@EruptDataProcessor("已注册数据源名称")
@Erupt(name = "xxxx")
public class Test {
    
}
```


> 原文: <https://www.yuque.com/erupt/giw1e5>