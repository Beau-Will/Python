import math#求勾股数写法一
x1=int(input("x1="))
y1=int(input("y1="))
z1=math.sqrt(x1**2+y1**2)
print(int(z1))#sqrt函数输出是浮点型，这里想要输出的勾股数是整数，因此加了int函数，输出是整数
from math import sqrt#写法二
x2=int(input("x2="))
y2=int(input("y2="))
z2=sqrt(x2**2+y2**2)
print(int(z2))