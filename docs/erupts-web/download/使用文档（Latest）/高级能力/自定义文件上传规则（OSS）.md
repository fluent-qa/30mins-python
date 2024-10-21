# 自定义文件上传规则（OSS ）


## 使用方法

**在Spring Boot入口类中增加 EruptAttachmentUpload** **注解，注解值为 AttachmentProxy 的实现类**
```java
@EruptAttachmentUpload(xxxxxx.class)
@SpringBootApplication
public class EruptDemoApplication {

    public static void main(String[] args) throws IOException, URISyntaxException {
        SpringApplication.run(EruptDemoApplication.class, args);
    }

}
```
**EruptAttachmentUpload 注解定义**
```java
// 仅需实现 AttachmentProxy 接口就可以自定义附件存储规则，如上传到 fastDFS 或者 OSS 中
public @interface EruptAttachmentUpload {
    Class<? extends AttachmentProxy> value();
}
```
**AttachmentProxy 接口说明**
```java
public interface AttachmentProxy {

    /**
     * @param inputStream 数据流
     * @param path        上传位置
     * @return 存储路径，正常情况下直接返回path参数即可
     */
    String upLoad(InputStream inputStream, String path);

    /**
     * 附件网络根地址
     *
     * @return
     */
    String fileDomain();

    /**
     * 是否同时保存到本地
     *
     * @return
     */
    default boolean isLocalSave() {
        return true;
    }
}
```



## 上传到七牛云存储示例

1. pom.xml中添加依赖
```xml
<dependency>
  <groupId>com.qiniu</groupId>
  <artifactId>qiniu-java-sdk</artifactId>
  <version>[7.2.0, 7.2.99]</version>
</dependency>
```

2. 新建QiniuOosProxy.java文件
```java
/**
 * 七牛对象存储demo
 *
 * @author yuepeng
 * @date 2020-05-17
 */
@Service
public class QiniuOosProxy implements AttachmentProxy {

    @Value("${qiniu.access_key}")
    private String accessKey; //你在七牛云申请的ACCESS_KEY

    @Value("${qiniu.secret_key}")
    private String secretKey; //你在七牛云申请的SECRET_KEY

    @Value("${qiniu.bucket}")
    private String bucket; //bucket名称

    @Override
    public String upLoad(InputStream inputStream, String path) {
        //根据存储地区创建上传对象
        UploadManager uploadManager = new UploadManager(new Configuration(Region.huanan()));
        String uploadToken = Auth.create(accessKey, secretKey).uploadToken(bucket);
        /*
         *	如果上传地址为 /2020-10-10/erupt.png
         *	在七牛云需通过 http://oos.erupt.xyz//2020-10-10/erupt.png才能访问
         *	访问地址带双斜杠，影响美观，所以做一下处理
         */
        path = path.startsWith("/") ? path.substring(1) : path;
        try {
            Response response = uploadManager.put(inputStream, path, uploadToken, null, MimeUtil.getMimeType(path));
            if (!response.isOK()) {
                throw new EruptWebApiRuntimeException("上传七牛云存储空间失败");
            }
            return "/" + path;
        } catch (QiniuException ex) {
            throw new EruptWebApiRuntimeException(ex.response.toString());
        }
    }

    @Override
    public boolean isLocalSave() {
        return false;
    }

    @Override
    public String fileDomain() {
        return "http://oos.erupt.xyz";
    }
}
```

3. 在spring boot入口类中增加EruptAttachmentUpload注解
```java
@SpringBootApplication
@EruptAttachmentUpload(QiniuOosProxy.class)
public class EruptDemoApplication {

    public static void main(String[] args) {
        SpringApplication.run(EruptDemoApplication.class, args);
    }

}
```

4. 由于图片根地址发证变化，所以需要修改app.js配置
```javascript
window.eruptSiteConfig.fileDomain: "http://xxxx.com"; // 具体oss的域名路径
```



> 原文: <https://www.yuque.com/erupt/famk6i>