# 开发自定义模块（拓展 erupt 功能模块）

可通过实现 EruptModule 接口，完成基于 erupt 的模块扩展
```java
@Component
public class EruptDemoModule implements EruptModule {

    static {
        EruptModuleInvoke.addEruptModule(EruptJpaAutoConfiguration.class);
    }
    
    // 模块信息
    @Override
    public ModuleInfo info() {
        return ModuleInfo.builder().name("erupt-tpl").build();
    }
    
    //初始化方法，每次启动时执行
    @Override
    public void run() {
        
    }

    // 初始化菜单 → 仅模块初始化时执行一次，标识文件位置.erupt/.${moduleName}
    @Override
    public List<MetaMenu> initMenus() {
        return null;
    }

    // 初始化方法 → 仅模块初始化时执行一次，标识文件位置.erupt/.${moduleName}
    @Override
    public void initFun() {
        
    }

}
```


> 原文: <https://www.yuque.com/erupt/fg2y4b>