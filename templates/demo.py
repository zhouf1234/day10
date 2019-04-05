class Person(object):
#面向对象的方法，先定义一个类Person，def在初始化调用，传参，最后的show调用

    def __init__(self,name,age):
        self.name=name
        self.age=age


    def show(self):
        if self.age>18:
            return '成年'
        else:
            return '未成年'


alex=Person('alex',19)
print(alex.name)
print(alex.show())