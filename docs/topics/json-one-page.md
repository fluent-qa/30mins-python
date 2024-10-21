# Revisited JSON - One Page

## 1. What is JSON?

> JSON（JavaScript Object Notation）是一种轻量级的数据交换格式，它使用人类可读的文本格式来存储和传输数据对象。  JSON 数据以键值对的形式组织，键是字符串，值可以是字符串、数字、布尔值、数组或其他 JSON 对象

### 1.1 JSON Examples

- key:value

```json
{ "name": "Kimi", "age": 1 }
```

- 数组

```json
["apple", "banana", "cherry"]
```

- 字符串，数字，布尔值

```json
"Hello, World!"
```

```json
4.2
```

```json
true
```

- 复杂对象

```json
{
  "key": "v1",
  "key2": "v2",
  "k_list": ["test","t2"],
  "k_obj": {"k1": "v1","k2": "v2"},
  "k_bool": true,
  "k_num": 4.3
}

```

## Code examples to read json

- json string to python object
- python object to json string
```python
import json
## string to python object
print(json.loads("{\"title\":\"Hello World\"}"))

json_str="""
{
  "key": "v1",
  "key2": "v2",
  "k_list": ["test","t2"],
  "k_obj": {"k1": "v1","k2": "v2"},
  "k_bool": true,
  "k_num": 4.3
}
"""
to_py_obj = json.loads(json_str)
print(to_py_obj)
print(type(to_py_obj))
## access python object
print(to_py_obj["key"])
print(to_py_obj["k_list"])
print(to_py_obj["k_bool"])
print(to_py_obj["k_num"])
print(type(to_py_obj["k_obj"]))

## python object to json string
result = json.dumps("Hello World") # to string
print(result)
print(json.dumps(4.3))
print(json.dumps("true"))
print(json.dumps(True))

## read
```
