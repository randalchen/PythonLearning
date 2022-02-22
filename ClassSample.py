class Person:
    count = 0  # 类属性
    __kind = 'Human'  # 私有的类属性，dir()可以查到为 _Person__kind

    # 构造器
    def __init__(self, name, age):
        self.name = name  # 实例属性
        self.age = age
        self.__country = 'China'  # 私有的实例属性
        Person.count += 1

    # 类方法，不能访问实例属性
    @classmethod
    def printcount(cls):  # cls 代表类本身
        print(cls.count)

    # 实例方法
    def say(self):
        print('我叫{0}，今年{1}岁。'.format(self.name, self.age))

    # 私有实例方法
    def __work(self):
        print('work hard!')

    # 使用装饰器,实现get,set方法
    @property
    def country(self):  # 为了调用方便，方法名可与私有属性保持一致
        return self.__country

    @country.setter  # 被property装饰的方法名.setter
    def country(self, country):  # 为了调用方便，方法名可与私有属性保持一致
        self.__country = country

    # 析构函数
    def __del__(self):
        print('释放资源')
        print('销毁实例对象{0}'.format(self))


# 创建实例对象
p1 = Person('张三', 12)
p1.say()
p1.country = "Japan"
print(p1.country)
p2 = Person('李四', 18)
p2.say()

print('共创建了{0}个对象'.format(Person.count))
Person.printcount()
del p1
del p2
