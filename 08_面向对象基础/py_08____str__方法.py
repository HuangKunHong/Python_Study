class Cat():

    def __init__(self, new_name):

        self.name = new_name

        print("%s 来了" % self.name)

    def __del__(self):

        print("%s  去了" % self.name)

    def __str__(self):

        # 必须 返回一个字符串
        return "我是[%s]" % self.name

tom = Cat("Tom")
print(tom)

