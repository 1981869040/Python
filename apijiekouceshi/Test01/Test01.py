# 新建 Python 文件
import requests

requests = requests.get('http://mirrors.sohu.com/')
print(requests.text)
