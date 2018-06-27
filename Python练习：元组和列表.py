# 题目1
var1 = [ 33, ['我的名字', '黑羽白月'], 'hello world!']
print(var1[2])
print(var1[-1])

# 题目2
var1 = [ 33, ['我的名字', '黑羽白月'], 'hello world!']
print(var1[1][1])
print(var1[-2][-1])

# 题目3
var1 = [ 33, ['我的名字', '黑羽白月'], 'hello world!']
var1[2] = 'Oh my God!'
print(var1)
var1[1][1] = '拜月童子'
print(var1)

# 题目4
var1 = [ 33, ('我的名字', '黑羽白月'), 'hello world!']
# var1[2][1] = '拜月童子'
var1[1] = ('我的名字', '拜月童子')
print(var1)


# 题目5
def func(arg):
    arg = 'hello'

var = 'ok'
func(var)
print(var)
# OK

def func(arg):
    arg[0] = 'hello'

var = ['ok']
func(var)
print(var)

# OK

def func(arg):
    arg = ['hello']

var = ['ok']
func(var)
print(var)

# OK
