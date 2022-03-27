# 新建 Python 文件
import random

a = random.randint(1, 10)
print(a)
xunhuan = 0
while xunhuan == 0:
    shuru = input("请输入数字：")
    shuru = int(shuru)
    if shuru == a:
        print("恭喜,猜中")
        break
    else:
        if shuru < 2:
            print("猜错,数字过小")
        else:
            print("猜错,数字过大")
print("游戏结束")
