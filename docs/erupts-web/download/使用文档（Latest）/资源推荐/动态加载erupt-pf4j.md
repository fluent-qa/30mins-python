# 动态加载erupt-pf4j

仓库地址：[https://github.com/snice/erupt-pf4j-demo](https://github.com/snice/erupt-pf4j-demo)
作者： 码农朱哲

## 使用方法
在导入erupt的前提下，导入erupt-pf4j依赖
```xml
<dependency>
   <groupId>com.github.snice</groupId>
   <artifactId>erupt-pf4j</artifactId>
   <version>0.0.1</version>
</dependency>
```

基于pf4j实现erupt体系中插件开发  
开发过程中，可以避免 修改erupt后重启，直接在管理端 重启下插件即可
生产环境，通过jar或zip，动态加载erupt，不需要重新部署  


> 原文: <https://www.yuque.com/erupt/gpgqg8>