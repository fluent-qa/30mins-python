# 代码编辑器 CODE_EDITOR


## 使用方法
```java
@Lob
@EruptField(
    views = @View(title = "代码编辑器"),
    edit = @Edit(title = "代码编辑器", 
                 type = EditType.CODE_EDITOR,
                 codeEditType = @CodeEditorType(language = "java"))
)
private String code;
```

## 配置项注解定义
```java
public @interface CodeEditorType {
    String language();  //编程语言，支持市面上所有主流编程语言，详见 `monaco editor` 
}
```


## 效果演示
![image.png](./img/upwKnCLig0fmm_72/1611567218492-147ff2e1-ae29-4946-962c-0443cb72a2c3-533275.png)
![image.png](./img/upwKnCLig0fmm_72/1611567270013-59bbd27d-82e4-43db-8696-fc36398c48f2-539175.png)


> 原文: <https://www.yuque.com/erupt/lhhquo>