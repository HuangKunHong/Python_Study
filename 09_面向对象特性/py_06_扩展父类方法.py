class Animal:
    def eat(self):
        print("吃---")
    def drink(self):
        print("喝---")
    def run(self):
        print("跑---")
    def sleep(self):
        print("睡---")

class Dog(Animal):

    def bark(self):
        print("汪汪叫")

class XiaoTianQuan(Dog):

    def fly(self):
        print("我会飞")
    def bark(self):
        # 1. 针对子类特有的需求，编写代码
        print("叫的跟神一样。。。")
        # 2. 使用super(). 调用原本在父类中看那个封装的方法
        super().bark()
        # 3. 增加其他子类的代码
        print("@#$%^&&**%$^&")
        # 4. 父类名.方法(self)
        Dog.bark(self)
        # 注意：如果使用子类调用方法，会出现递归调用 - 死循环！
        # XiaoTianQuan.bark(self)
xtq = XiaoTianQuan()

# 如果子类中重写了父类的方法
# 在使用子类对象调用方法时，会调用子类中重写的方法
xtq.bark()
