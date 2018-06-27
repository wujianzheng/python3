# 题目1
def health():
    stature = input('请输入你的身高(单位米):')
    weight = input('请输入你的体重(单位公斤):')
    age = input('请输入你的年龄:')
    intstature = float(stature)
    intweight = float(weight)
    calculate = intweight / (intstature ** 2)
    intage = int(age)
    if intage < 10:
        print('10岁以下儿童不参与健康评估。')
        return
    elif intage >= 10 and intage <60:
        if calculate > 24:
            print('体重超重')
        elif calculate < 18:
            print('体重超轻')
        else:
            print('体重正常')
    else:
        print('60岁以上老人不参与健康评估')
health()


height = input('请输入你的身高(单位 米):')
# 转化为浮点数
intHeight = float(height)

weight = input('请输入你的体重(单位 公斤):')
# 转化为浮点数
intWeight = float(weight)


age = input('请输入你的年龄:')
# 转化为整数
intAge = int(age)

if  intAge < 10 :
    print('10岁以下儿童不参与健康评估')

elif intAge < 60:
    # bmi 变量代表健康指数
    bmi = intWeight / (intHeight**2)

    if bmi > 24 :
        print('您的体重偏重了')
    elif bmi < 18 :
        print('您的体重偏轻了')
    else:
        print('您的体重正常')
else:

    print('60岁以上老人不参与健康评估')
