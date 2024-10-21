# 布局定义 @Layout

版本支持：1.12.0及以版本

### 代码示例
```java
@Erupt(
       name = "Erupt",
       orderBy = "EruptTest.no desc",
       layout = @Layout(
           // 固定前三列
           tableLeftFixed = 3, 
           // 使用前端分页
           pagingType = Layout.PagingType.FRONT,
           // 每页显示20条数据
           pageSize = 20
        )
)
public class EruptTest extends BaseModel {
    
	
}
```


### 注解定义
```java
public @interface Layout {

    //表单大小
    FormSize formSize() default FormSize.DEFAULT;

    //表格左侧列固定数量
    int tableLeftFixed() default 0;

    //表格右侧列固定数量
    int tableRightFixed() default 0;

    //分页方式
    PagingType pagingType() default PagingType.BACKEND;

    //分页大小
    int pageSize() default 10;

    //可选分页数
    int[] pageSizes() default {10, 20, 30, 50, 100, 300, 500};

    // 页面数据更新时间，单位：毫秒 1.12.13 及以上版本支持
    int refreshTime() default -1;


    enum FormSize {
    	//默认布局，每行显示三个表单组件
        DEFAULT, 
    	//整行布局，每行显示一个表单组件
        FULL_LINE
    }

	enum PagingType {
        //后端分页
        BACKEND,
        //前端分页
        FRONT,
        //不分页，最多显示：pageSizes[pageSizes.length - 1] * 10 条
        NONE
    }

}
```

### 整行布局 FULL_LINE
![image.png](./img/1O-rZ8Lgr6MCDio2/1688309619970-853a4af2-a7ae-4d6b-afa6-1322e9d97631-957321.png)

### 列固定 Fixed
![image.png](./img/1O-rZ8Lgr6MCDio2/1688309683756-75a1cd26-783b-4ed4-a023-8e5915058cdb-291821.png)



> 原文: <https://www.yuque.com/erupt/abgsh10xr7nrkzga>