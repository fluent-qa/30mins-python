# Pytest 如何使用切换被测试环境

<!-- TOC -->

* [Pytest 如何使用切换被测试环境](#pytest-如何使用切换被测试环境)
    * [0-问题: 如何让同一份代码在不同环境运行](#0-问题-如何让同一份代码在不同环境运行)
    * [1-dynaconf 管理所有环境信息](#1-dynaconf-管理所有环境信息)
    * [2. pytest- 通过命令行切换环境](#2-pytest--通过命令行切换环境)
    * [3. 命令行运行](#3-命令行运行)

<!-- TOC -->

下面介绍一个使用第三方库结合pytest机制，给pytest 新增一个命令行参数实现所有不同环境信息在一个文件并且可以切换被测试环境的例子，
代码量实际上非常少，但是起作用的.

## 0-问题: 如何让同一份代码在不同环境运行

运行自动化测试的时候，最理想状态就是同一份代码在不同的环境中运行，那么如何让pytest运行时候切换运行环境呢？
一般会想到的就是配置文件，不同的配置文件对应不同的环境，然后通过环境变量去切换使用不同的配置文件.

这里尝试所有***不同环境配置信息***都在***一个文件***中，也可以在运行是切换环境的做法.

## 1-dynaconf 管理所有环境信息

使用dynaconf管理环境信息, 配置文件在一份toml文件中，示例如下:

```toml
[default]
db = { url = "postgresql://postgres:changeit@localhost:7432/test_hub" }
[dev]
db_url = "postgresql://postgres:changeit@localhost:7432/test_hub"
[test]
db_url = "postgresql://postgres:changeit@test:7432/test_hub"
[product]
db_url = "postgresql://postgres:changeit@prod:7432/test_hub"
[product_new]
db_url = "postgresql://postgres:changeit@prod_new:7432/test_hub"
```

上面文件代表了四个环境的的db_url值，分别是***dev/test/product/product_new***

如何通过dynaconf获取这些不同的环境信息呢？

-
    1. 首先获取配置信息, 所有在***settings.toml***文件中的配置信息都初始化加载

```python
from dynaconf import Dynaconf

settings = Dynaconf(
    settings_file=["configs/settings.toml", "configs/.secrets.toml",
                   "settings.toml", ".secrets.toml"],
    environment=True,
    load_dotenv=True,
    dotenv_path="/.env",  # custom path for .env file to be loaded
    includes=["../config/custom_settings.toml"],
)

settings.validators.validate()
```

-
    2. 获取默认信息：直接使用settings.db_url就可以获取

```python
@allure.feature("getting default db_url")
def test_get_default_settings():
    logging.info(settings.db_url)
    assert settings.db_url == "postgresql://postgres:changeit@default:7432/test_hub"
```

返回的是默认的db_url: postgresql://postgres:changeit@default:7432/test_hub

-
    3. 获取其他环境的信息：

切换获取那个环境信息

```python
def ensure_env_settings(env_name: str):
    env_switcher_key = settings.ENV_SWITCHER_FOR_DYNACONF
    os.environ[env_switcher_key] = env_name
    settings.reload()

```

获取新的环境变量：切换环境之后，再获取db_url,这个时候就变成了test环境的db_url:postgresql://postgres:changeit@test:
7432/test_hub

```python
@allure.feature("getting test env db_url")
def test_get_test_env_db_url():
    ensure_env_settings("test")
    print(settings.db_url)
```

## 2. pytest- 通过命令行切换环境

上面说明了环境配置切换的原理，那么结合pytest 就是接收一个名行行参数 ***env***,然后根据这个命令行参数去获取不同环境配置，
实现也算比较简单，只要在 tests目录下的***conftest.py***文件中实现:

1. 定义新命令行参数
2. 接收此命令行参数并进行切换环境参数
3. 之后就可以直接使用此配套环境的参数了

定义新命令行参数:

```python
## 定义新的命令行参数
def pytest_addoption(parser):
    parser.addoption("--env", action="store", default="dev",
                     help="Environment to run tests in")
```

接收命令行参数值到request并且实现切换环境参数:

```python
@pytest.fixture(scope="session", autouse=True)
def setup_environment_setting(request):
    env_name = request.config.getoption("--env")
    ensure_env_settings(env_name)
```

## 3. 命令行运行

这个时候针对步骤1中的那个测试运行以下四个环境参数的命令,就会得到不同的测试结果了，
也就是这个环境变量***生效了***.

```shell
poetry run pytest tests/test_settings.py --evn default
poetry run pytest tests/test_settings.py --evn test
poetry run pytest tests/test_settings.py --evn product
poetry run pytest tests/test_settings.py --evn product_new
```

## 4. 小结和几个衍生的问题

- Dynaconf第三方库可以通过一个文件就可以管理所以环境变量参数，同时支持直接通过属性名访问***settings.db_url***这种方式
- pytest 创建一个新的参数的方法是什么？
- pytest fixture的作用是什么？
- pytest fixture里面request指的是什么？














