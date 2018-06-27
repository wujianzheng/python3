myFavorit = '我最爱的运动有：'
sport1 = '足球'
sport2 = '蓝球'
print( myFavorit + sport1 + '---' + myFavorit + sport2 )


hello = '刘总你好啊'
print(hello[2:4])

str1 = '小张：79 + 小李：88 | 小赵：83'
pos1 = str1.split('+')
print(str1)
print(pos1)

a = [1, 2, 3.14, 'hello']  

# append 之后，a就变成了 [1, 2, 3.14, 'hello', '你好']
a.append('你好')
print(a)

  
# 继续append ，a就变成了 [1, 2, 3.14, 'hello', '你好', [7,8]]
a.append([7,8])
print(a)

salary = input('请输入薪资：')

# 计算出缴税额，存入变量tax
tax = int(salary) *25/100  

# 计算出税后工资，存入变量aftertax
aftertax = int(salary) *75/100 

print('税前薪资是：%s 元， 缴税：%s 元， 税后薪资是：%s 元' %
(salary,tax,aftertax))
