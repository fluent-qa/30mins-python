# ⚔️ 自定义数据逻辑（ DataProxy ）

提供增、删、改、查、导入、导出、数据初始化等事件触发逻辑接口，**相当于传统开发中的 service 层**

可以实现如：缓存写入，消息推送，数据校验，RPC调用，动态赋值等功能 ！

new 支持合计行、自定义行、搜索项默认值、表单默认值、excel导出workbook对象后置操作等特性



## 使用方法
在 @Erupt 注解中添加 dataProxy 配置，重写其中的方法即可
```java
@Erupt(name = "Erupt", dataProxy = EruptTestDataProxy.class)
public class EruptTest extends BaseModel{
    
	@EruptField(
            views = @View(title = "名称"),
            edit = @Edit(title = "名称")
    )
    private String name;
    
}
```
```java
@Service //添加此注解可使用依赖注入相关功能
public class EruptTestDataProxy implements DataProxy<EruptTest>{
    
    @Override
    public void beforeAdd(EruptTest eruptTest) {
        //数据校验
        if("张三".equals(eruptTest.getName())){
			throw new EruptApiErrorTip("名称禁止为张三！");
        }
    }

    @Override
    public void beforeUpdate(EruptTest eruptTest) {
        //动态写数据
        eruptTest.setName(eruptTest.getName() + "xxxxxxx");
    }

    @Override
    public void beforeDelete(EruptTest eruptTest) {
        //TODO 删除前事件处理逻辑
    }
    
    @Override
    public void afterFetch(Collection<Map<String, Object>> list) {
        //TODO 查询结果动态处理
    }
    
    @Override
    public void addBehavior(EruptTest eruptTest) {
        //TODO 数据初始化逻辑
    }
    
    ......
    依据实际情况重写相关功能的方法
}
```

## 

## DataProxy接口定义
```java
public interface DataProxy<MODEL> {

    /**
     * 新增前
     *
     * @param model 待新增对象数据
     */
    default void beforeAdd(MODEL model) {
    }

    /**
     * 新增后
     *
     * @param model 已新增对象数据
     */
    default void afterAdd(MODEL model) {
    }

    /**
     * 修改前
     *
     * @param model 待修改对象数据
     */
    default void beforeUpdate(MODEL model) {
    }

    /**
     * 修改后
     *
     * @param model 已修改对象数据
     */
    default void afterUpdate(MODEL model) {
    }

    /**
     * 删除前
     *
     * @param model 待删除对象数据
     */
    default void beforeDelete(MODEL model) {
    }

    /**
     * 删除后
     *
     * @param model 已删除对象数据
     */
    default void afterDelete(MODEL model) {
    }

    /**
     * 查询前动态注入条件
     * @param conditions 前端已传递条件，如果某个条件可做 remove 等操作，通过返回值做额外条件处理
     *
     * @return 自定义查询条件(HQL语句)，列占位符用字段名，可做 OR 拼接等操作，如：(xxx.id = 'a' or name = 'b')
     */
    default String beforeFetch(List<Condition> conditions) {
        return null;
    }

    /**
     * 查询结果处理
     *
     * @param list 查询结果
     */
    default void afterFetch(Collection<Map<String, Object>> list) {
    }


    /**
     * 数据新增行为，对数据做初始化操作
     */
    default void addBehavior(MODEL model) {
    }

    /**
     * 数据编辑行为，对待编辑的数据做预处理
     */
    default void editBehavior(MODEL model) {
    }

    /**
     * excel导出
     *
     * @param wb POI文档对象，需要强制转换为Workbook类型
     */
    default void excelExport(Object wb) {
    }

    /**
     * exceld导入（1.10.14及以上版本支持）
     *
     * @param wb POI文档对象，需要强制转换为Workbook类型
     */
    default void excelImport(Object wb) {
    }
   
    /**
     * 自定义行
     *
     * @param  conditions 查询条件
     * @return 自定行列对象
     */
    default List<Row> extraRow(List<Condition> conditions) {
        return null;
    }

    /**
     * 默认查询条件 (1.10.11及以上版本支持)
     *
     * @param  conditions 查询条件
     */
    default void searchCondition(Map<String, Object> condition) {

    }
    

}

```

## 

## 自定义行
[自定义行（合计行）](https://www.yuque.com/erupts/erupt/yi6gl3?view=doc_embed)


> 原文: <https://www.yuque.com/erupt/nicqg3>