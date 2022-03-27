# 新建 Python 文件

class Cat(object):
    print("这是一个类")

    def __init__(self, a, b, c="默认"):
        self.name = a
        self.age = b
        self.c = c

    # def set_a(self, a):
    #     self.name = a
    #
    # def set_b(self, b):
    #     self.age = b

    def Chi(self):
        """
        :param self:
        :return:
        """
        print(self.c)
        print("我叫：{},今年：{} 岁".format(self.name, self.age))
