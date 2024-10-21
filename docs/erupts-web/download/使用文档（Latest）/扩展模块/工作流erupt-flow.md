# 工作流 erupt-flow

仓库地址：[https://github.com/hlhutu/erupt/tree/flow/erupt-extra/erupt-flow](https://github.com/hlhutu/erupt/tree/flow/erupt-extra/erupt-flow)
作者： **TOMDOG9527 (QQ:**749863487 **)**

# 插件简介
**完全零技术的自定义流程+自定义表单。无需技术，小白用户皆可使用。**
前端基于vue+elemntui开发，风格参考于钉钉的审批。
后端基于erupt框架的自研流程引擎，设计思路参考acvititi。

- 演示地址：[http://119.23.65.238:8080/](http://119.23.65.238:8080/)
- 账号密码：erupt/erupt123（请勿修改密码！）

![image.png](./img/hf0Dp9kR8fYSZ1Om/1682506237770-e6d7ac6f-97bc-481f-9a6e-8076cd980ffe-677260.png)
![image.png](./img/hf0Dp9kR8fYSZ1Om/1682506216962-68f4b7ed-efc7-4e68-81ab-e95a197ec171-287442.png)
![image.png](./img/hf0Dp9kR8fYSZ1Om/1682506257670-184abbcd-061d-4a59-9254-cf7c6846691b-028712.png)
![image.png](./img/hf0Dp9kR8fYSZ1Om/1682506306299-0e5237ed-24ad-4349-9d45-5bac5f4235d6-051909.png)

# 快速开始

## 导入依赖
```xml
<dependency>
  <groupId>xyz.erupt</groupId>
  <artifactId>erupt-flow</artifactId>
  <!-- 版本号与erupt同步 -->
  <version>${erupt.version}</version>
</dependency>
```

## 重启项目
登录之后，可以看到自动生成了几个菜单
![image.png](./img/hf0Dp9kR8fYSZ1Om/1684742391992-78117dc4-6934-450f-ae25-3a87a7cb34cd-770839.png)

## 绘制流程图
在“后台管理”绘制流程图
![image.png](./img/hf0Dp9kR8fYSZ1Om/1684742550705-71fc7bd5-4508-4299-a729-1b4b3fd144f7-155249.png)
按步骤操作
![image.png](./img/hf0Dp9kR8fYSZ1Om/1684742582976-9dd34d4f-4899-459c-9f49-01edfa22275e-564452.png)
![image.png](./img/hf0Dp9kR8fYSZ1Om/1684742627299-5353486d-6f0f-4fb9-a80c-46a1f6c6de16-767527.png)
![image.png](./img/hf0Dp9kR8fYSZ1Om/1684742716930-2a58960f-051e-429f-b098-6afe52697f03-703669.png)
绘制完成点击右上角发布即可
![image.png](./img/hf0Dp9kR8fYSZ1Om/1684742766342-7ac73da0-be29-425d-bdb9-0ffc3fc1c114-391697.png)


## 发起流程
发布成功后，在“工作区”发起工单
![image.png](./img/hf0Dp9kR8fYSZ1Om/1684742840946-43ebbe06-d67d-4341-ad64-5cc919f7fd7d-372944.png)
填写表单然后提交
![image.png](./img/hf0Dp9kR8fYSZ1Om/1684742874816-25e85ecb-ea2a-4a80-bc62-e525d407e60a-301565.png)
工作流会流转到下一个需要处理用户。在他的“待我处理”中可以进行处理
这里为了方便，我把审批人改成发起人自己。![image.png](./img/hf0Dp9kR8fYSZ1Om/1684743014095-c786509f-2194-44ca-9079-db2bc9580207-435059.png)
在“我的工单”下，可以看到自己发起或者处理过的所有工单
![image.png](./img/hf0Dp9kR8fYSZ1Om/1684743067955-84e97d49-dec3-4b11-a90f-d0e28f6f3c20-312566.png)

## @EruptFlowForm 注解
@EruptFLowForm注解，可以用于所有标记为@Erupt的实体类。用于将这个实体解析为erupt-flow中的表单

1. 标记注解
```java
//必须有@Erupt注解，才可以使用这个注解
@EruptFlowForm
@Erupt(name="请假")
@Entity
@Data
public class DemoLeave {

    //主键
    @Id
    @GeneratedValue(generator = "generator")
    @GenericGenerator(name = "generator", strategy = "native")
    @Column(name = "id")
    @EruptField
    private Long id; //如果继承BaseModel则不能再重复声明id

    @EruptField(
            views = @View(title = "请假人"),
            edit = @Edit(title = "请假人")
    )
    private String person;

    @EruptField(
            views = @View(title = "请假天数"),
            edit = @Edit(title = "请假天数")
    )
    private Integer days = 1;
}
```

2. 重启项目

![image.png](./img/hf0Dp9kR8fYSZ1Om/1684743766736-3ace7d7e-1ec5-403c-8d1c-8645b79dcf0a-182802.png)
这里会打印有几个Erupt Flow Form 被识别

3. 绘制流程图

在“表单”界面，可以看到“Erupt表单”
![image.png](./img/hf0Dp9kR8fYSZ1Om/1684743431172-e4b9f581-b483-49e1-8880-2db6b9918119-818472.png)
点击即可将实体类中的字段，解析到表单
![image.png](./img/hf0Dp9kR8fYSZ1Om/1684743464719-8d7d6b06-863b-4a27-9030-6681941935a3-220540.png)
> 注意！！！@EruptFlowForm并未实现所有@Erupt的功能。解析完之后请检查一下字段。
> 你也可以手动调整任何字段。


# 已知的bug

## 1.12.0

1. 项目有context-path的情况下，flow上传图片显示404

解决办法：无解。只能不用context-path路径
![image.png](./img/hf0Dp9kR8fYSZ1Om/1689217479972-878f2a49-ec33-4621-95d0-5b74ed89b0cb-974334.png)

2. 表单字段后面，有诸如 [E]、[R]等字样。这是调试信息，不影响使用

## 1.11.7

1. **工作区和后台管理页面404**

系统管理 -> 菜单管理 中，找到这2个页面，去掉路径前缀的 erupt-api
![image.png](./img/hf0Dp9kR8fYSZ1Om/1686191141447-f37605e9-684b-45f3-aa62-03456b9270ce-293405.png)

2. **流程发布报错**

添加OaProcessDefinition类的主键生成策略
![image.png](./img/hf0Dp9kR8fYSZ1Om/1686191098013-7405f40f-27ee-442e-9127-c12ce63d025f-508131.png)

# 前后端分离
插件默认的菜单路径，仅支持前后端不分离部署。如需前后端分离部署，需要修改菜单路径
![image.png](./img/hf0Dp9kR8fYSZ1Om/1689217397306-f950cb07-62c4-40d5-a6db-69381e41f836-512391.png)


> 原文: <https://www.yuque.com/erupt/sd27r9o1pex1s5xn>