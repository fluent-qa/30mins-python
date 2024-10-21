
# pytest fixture 使用要点

pytest fixtures 提供了一种方法来为测试提供共享状态。它们允许你定义一些代码，这段代码在测试函数执行之前或之后运行，以便为测试设置或清理环境。

## 使用要点

### 基本使用

fixtures 通过使用 `@pytest.fixture` 装饰器定义。

```python
import pytest

@pytest.fixture
def sample_user():
    return {"name": "John Doe"}
```

### 作为测试函数参数

fixtures 可以通过将其作为参数传递给测试函数来使用。

```python
def test_user_name(sample_user):
    assert sample_user["name"] == "John Doe"
```

### 使用 scope 参数

fixtures 可以有三种不同的生命周期（scope）：

- `function`：每个测试函数都会重新创建 fixture。
- `class`：一个类中所有测试共享一个 fixture 实例。
- `module`：一个模块内所有测试共享一个 fixture 实例。
- `session`：整个测试会话共享一个 fixture 实例。

```python
@pytest.fixture(scope="class")
def db_connection(request):
    # setup db connection
    connection = get_db_connection()
    def teardown():
        # teardown db connection
        connection.close()
    request.addfinalizer(teardown)
    return connection
```

### 使用 autouse 参数

如果希望 fixture 在每个测试中自动使用，可以设置 `autouse=True`。

```python
@pytest.fixture(autouse=True)
def enable_feature_flag():
    # enable a feature flag for all tests
    set_feature_flag(True)
```

### 使用 yield 进行资源管理

使用 `yield` 可以确保在测试之后执行清理代码。

```python
@pytest.fixture
def temp_file():
    path = create_temp_file()
    yield path
    # 测试结束后删除临时文件
    remove_temp_file(path)
```

### 请求参数

fixture 函数中的 `request` 对象可以用于访问参数、测试函数和 fixture。

```python
@pytest.fixture
def another_fixture(dependency_fixture):
    request.some_arg = dependency_fixture
```

## 示例代码

假设我们有一个数据库连接的 fixture，我们希望在每个测试函数之前建立连接，在测试之后关闭连接。

```python
import pytest

@pytest.fixture
def db_session():
    db = Database.connect()
    yield db
    db.close()

def test_db_connection(db_session):
    assert db_session.is_connected() is True

def test_db_query(db_session):
    result = db_session.query("SELECT * FROM users")
    assert len(result) > 0
```

在这个例子中，`db_session` fixture 为每个测试提供了一个数据库连接，并确保在测试执行完毕后关闭连接。

---

pytest fixtures 是一种强大的工具，可以帮助你编写更干净、更高效的测试。通过使用 fixtures，你可以轻松地在测试之间共享资源，减少重复代码，并更好地管理测试环境。
```

这份文档提供了 pytest fixtures 的使用要点和示例代码，适合希望深入了解如何使用 fixtures 来提高测试代码质量的 Python 工程师。