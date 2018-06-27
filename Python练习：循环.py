# 题目1
str1 = '''
熊宁
杰益
王伟伟
青芳
玉琴
焦候涛
莫福
杨高旺
唐欢欢
韩旭
'''
       
str2 = '''
焦候涛 
熊宁 
玉琴 
骆龙 
韩旭 
杨高旺
杰益  
莫福  
伟伟
李福  
'''
print(len(str1))
print(len(str2))
str3 = []
for str3 in str1:
    if str1 not in str2:
        print(str3)
        


