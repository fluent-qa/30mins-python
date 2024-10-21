# 富文本编辑器 HTML_EDITOR


## 使用方法
```java
@Lob  //富文本编辑器所产生的文本量较大，所以设置为长字符串类型在数据库中存储
@EruptField(
    edit = @Edit(title = "内容(UEditor)", 
                 type = EditType.HTML_EDITOR, 
                 htmlEditorType = @HtmlEditorType(HtmlEditorType.Type.UEDITOR))
)
private String content;
```

## 配置项注解定义
```java
public @interface HtmlEditorType {

    Type value(); //富文本文本编辑器类别

    enum Type {
        CKEDITOR,   // https://ckeditor.com/ckeditor-5/
        UEDITOR     // http://fex.baidu.com/ueditor/
    }
}
```

## 效果演示
UEditor
![image.png](./img/aWpAXHBPTAC2hUag/1611567396761-5cbae6b2-2a3f-4d60-ad30-e853cec8c6bd-213747.png)
CkEditor
![image.png](./img/aWpAXHBPTAC2hUag/1611567475270-e0d4b5b0-0e93-4a92-b529-28479c62322d-738789.png)



> 原文: <https://www.yuque.com/erupt/gebgnr>