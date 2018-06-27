# 题目1
var1 = [ 33, ['我的名字', '黑羽白月'], 'hello world!']
print(var1)
var1.append('你好')
print(var1)

# 题目2
var1 = [ 33, ['我的名字', '黑羽白月'], 'hello world!']
print(var1)
var1.insert(0, '你好')
print(var1)

# 题目3
var1 = [ 33, ['我的名字', '黑羽白月'], 'hello world!']
print(var1)
var1.insert(1, '你好')
print(var1)

# 题目4
str1 = '大家好，我的名字叫：黑羽白月'
print(str1)
print(str1[str1.find('黑羽白月'):])
print(str1[str1.find('：') + 1 :])

# 题目5
str1 = '大家好，我的名字叫：黑羽白月'
str2 = str1.split('：')
print(str2)
print(str2[1])
print(str1.split('：')[1])
