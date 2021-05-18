#第一题
'''
def jushu_score(a=1,b=100):
    sum1=0
    for k in range(a,b+1):
        if k%2==1:
            sum1+=k
    return sum1
print(jushu_score(3,9))
#第二题
def avg_score(**kwargs):
    for i,j in kwargs.items():
        print('%s的平均分是%d'%(i,sum(j)/len(j)))
avg_score(张三=[90,60,88],李四=[75,100,85],王五=[68,95,70])
#第三题
def feibonaqi(n):
    if n==1 or n==2:
        ret=1
    else:
        ret=feibonaqi(n-1)+feibonaqi(n-2)
    return ret
print(feibonaqi(6))
'''
#第四题
x=100 #全局变量
def myfunction():
    x=10 #局部变量
    x+=10
    #global x
    #x+=10
    def function_in():
        global x #全局变量x，unlocal为引用外部变量
        x+=5
        print(x)
    function_in()
    print(x)
myfunction()
print(x)
'''
#第五题
import  random
def a(n):
    def inner(func):
        def c(function):
            for i in range(n):
                function.append(random.randint(1,20))
           
            return func(function)
            
        return c
    return  inner
@a(20)
def chuer(d):
    ff = lambda x: x + 1 if (x + 1) % 2 == 0 else ''
    c = list(map(ff, d))
    while '' in c:
        c.remove('')
    return c
print(chuer([]))
'''



