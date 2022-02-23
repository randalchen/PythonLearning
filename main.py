# 这是一个示例 Python 脚本。

# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。
from random import randrange


def print_hi(name):
    # 在下面的代码行中使用断点来调试脚本。
    print(f'Hi, {name}')  # 按 Ctrl+F8 切换断点。


# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    print_hi('PyCharm')
print('*' * 100)
# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助

# while语句实现斐波那契数列
a, b = 0, 1
while a < 1000:
    print(a, end=',')
    a, b = b, a + b
print('')
print('*' * 100)

# if语句测试
# x = int(input("请输入一个整数: "))
x = randrange(-100, 100)
if x > 0:
    print(x, '是正整数')
elif x < 0:
    print(x, '是负整数')
else:
    print(x, '为零')
print('*' * 100)

# for语句示例，中括号是数组
# break 语句和C 中的类似，用于跳出最近的for 或while 循环
# 循环的else 子句则在未运行break 时执行。
# continue 语句也借鉴自C 语言，表示继续执行循环的下一次迭代
words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))
print('*' * 100)

for i in range(5):
    print(i)
# Create a sample collection
users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}
# Strategy: Iterate over a copy
for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]
print(users)
# Strategy: Create a new collection
users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}
active_users = {}
for user, status in users.items():
    if status == 'active':
        active_users[user] = status
print(active_users)
print('*' * 100)

# sum() 是一种把可迭代对象作为参数的函数：
print(sum(range(4)))  # 0 + 1 + 2 + 3
print('*' * 100)

# Flask Web开发框架

# test 2022-2-23-14：36
