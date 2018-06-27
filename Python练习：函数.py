# 题目1
def information(name, age):
    print("他的名字是：" + name)
    print("他的年龄是：" + str(age))
information('小王', 18)
information('关羽', 28)
information('赵云', 24)

# 有两个参数
def getNameAge(str1, str2):
    # 用切片获取第1个参数的人名
    name = str1[-2:]

    # 用切片获取第2个参数的 年龄
    age = str2[-2:]

    # 将人名和 年龄连起来，中间是冒号

    ret = name + ':' + age

    # 别忘了， 最后一定要使用return 返回结果
    return ret

# 不指定参数名的调用
name_age1 = getNameAge('他的名字是：关羽','他的年龄是：28')
# 打印出返回结果
print(name_age1)


# 指定参数名的调用
name_age2 = getNameAge(str1='他的名字是：赵云',str2='他的年龄是：24')
# 打印出返回结果
print(name_age2)

# 题目2
def testfunc(arg1,arg2): 
    return (arg1 + arg2)

# testfunc(1)
testfunc(1,2)
testfunc(arg1=1,arg2=2)
testfunc(arg2=2,arg1=1)
# testfunc(arg1=1,2)    
testfunc(1,arg2=2)

# 题目3
def func1(num1,num2):
    return num1**2 + num2**2
# 返回num1**2 + num2**2的值

def func2(num1,num2):
    print(num1**2 + num2**2)
# 打印num1**2 + num2**2的值
