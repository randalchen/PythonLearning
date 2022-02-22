class Person:

    def __call__(self, name):
        print('姓名：{0}'.format(name))
        return dict(name=name)


p1 = Person()
a = p1('张三')
print(a)