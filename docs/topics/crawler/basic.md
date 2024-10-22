## 爬虫

- API获取数据
- 网页获取数据
  * 浏览器静态数据
  * 浏览器动态数据
  * 无痕浏览器
- 工具：
   * httpx/request
   * UI: DrissionPage/Selenium/Playwright
   * RPA: 影刀/八爪鱼/RobotFramework/RPA工具

### 1. httpx/requests

- install: 
  * ```pdm add "httpx[all]" ```
  * ```pdm add requests```

### 1.1 httpx/requests demo

Getting Data from API:



```python
import asyncio

import httpx
import requests

async def post_data():
    data = {'name': 'crawler','email':'crawler@gmail.com'}
    async with httpx.AsyncClient() as client:
        response = await client.post('https://httpbin.org/post', data=data)
        print(response.json())
      
def httpx_get():
  url = "https://httpbin.org/anything/anything"
  response = httpx.get(url)
  print(response.json())
  
def get_data():
  url = 'https://httpbin.org/get'

def requests_get_data():
  url = "https://httpbin.org/anything/anything"
  
  payload = {}
  headers = {}
  response = requests.request("GET", url, headers=headers, data=payload)
  print(response.text)


# asyncio.run(post_data())
httpx_get()
requests_get_data()
```
## 2. UI 

installation:

- pdm add DrissionPage
```python
from DrissionPage import Chromium
# from DrissionPage import WebPage
# from DrissionPage import SessionPage
# from DrissionPage import SessionOptions
# from DrissionPage.common import Settings
# from DrissionPage.common import Keys
# from DrissionPage.common import By
# from DrissionPage.common import wait_until
# from DrissionPage.common import make_session_ele
# from DrissionPage.common import configs_to_here
# from DrissionPage.errors import ElementNotFoundError
# from DrissionPage.items import SessionElement
# from DrissionPage.items import ChromiumElement
# from DrissionPage.items import ShadowRoot
# from DrissionPage.items import NoneElement
# from DrissionPage.items import ChromiumTab
# from DrissionPage.items import MixTab
# from DrissionPage.items import ChromiumFrame
from DrissionPage import ChromiumOptions


# tab = Chromium().latest_tab
# tab.get('https://DrissionPage.cn')
# tab.close()

def set_chromium_options():
  path = r'D:\Chrome\Chrome.exe'  # 请改为你电脑内Chrome可执行文件路径
  ChromiumOptions().set_browser_path(path).save()

def gitee_login():
  # 启动或接管浏览器，并创建标签页对象
  tab = Chromium().latest_tab
  # 跳转到登录页面
  tab.get('https://gitee.com/login')
  
  # 定位到账号文本框，获取文本框元素
  ele = tab.ele('#user_login')
  # 输入对文本框输入账号
  ele.input('您的账号')
  # 定位到密码文本框并输入密码
  tab.ele('#user_password').input('您的密码')
  # 点击登录按钮
  tab.ele('@value=登 录').click()

gitee_login()


```
