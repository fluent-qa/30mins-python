# 文件上传 ATTACHMENT

**使用需确认application.yml中是否存在erupt.uploadPath 属性，该属性表示附件存储的实际物理位置。**

**附件存储路径为：上传日期 + 随机字符串 + 格式 → /2020-11-15/tpq1l9.png**

想更改命名规则详见：[自定义附件上传规则（OSS 七牛云示例）](https://www.yuque.com/go/doc/15145352?view=doc_embed)

不希望将图片存储于本地磁盘中详见：[自定义附件上传规则（OSS 七牛云示例）](https://www.yuque.com/go/doc/15145352?view=doc_embed)


## 使用方法
```java
@EruptField(
    views = @View(title = "文件上传"),
    edit = @Edit(title = "文件上传", type = EditType.ATTACHMENT,
                 attachmentType = @AttachmentType)
)
private String attachment;
```

## 配置项注解定义
```java
public @interface AttachmentType {

    long size() default 0; //上传文件大小限制

    String path() default ""; //文件存储附加路径

    String[] fileTypes() default {}; //允许上传的文件类型，不填表示允许任何类型

    Type type() default Type.OTHER; //上传方式

    int maxLimit() default 1; //上传数量限制

    ImageType imageType() default @ImageType;

    String fileSeparator() default "|"; //由于存储方式为单列，所以要定义多图片上传路径的分隔字符

    enum Type {
        BASE,  //可上传任意文件
        IMAGE, //图片上传
    }

    @interface ImageType {
        
        //宽高使用长度为2的数组，第一位是最小宽高限制，第二位是最大宽高限制
        int[] width() default {};

        int[] height() default {};
    }

}
```

## 代码演示

#### 图片上传
```java
@EruptField(
    views = @View(title = "图片"),
    edit = @Edit(title = "图片", type = EditType.ATTACHMENT,
                 attachmentType = @AttachmentType(type = AttachmentType.Type.IMAGE, maxLimit = 3))
)
private String pic;
```

#### 上传pdf
```java
@EruptField(
    edit = @Edit(title = "上传PDF文件", type = EditType.ATTACHMENT,
                 attachmentType = @AttachmentType(fileTypes = "pdf"))
)
private String pdf;
```


## 效果演示
![image.png](./img/MOZbLH7qgi3Q4Sh6/1611567034171-97444755-9424-4774-af8c-89b537c4a7c3-609460.png)
![image.png](./img/MOZbLH7qgi3Q4Sh6/1611567143247-2300b9b5-a458-41fd-8082-ebf0834a9fb2-244716.png)


> 原文: <https://www.yuque.com/erupt/lsm2d0>