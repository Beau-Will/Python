s="hello,python" \
  "wow"#定义字符串类型变量 \为转义符
print(s)
print(s[1:3])#字符串切片 区间左闭右开 同时也说明字符串s的第一个字母对应数字“0”
print(s[1-3])#这里的1-3是做减法1-3=-2，即取字符串s的倒数第二个字母
num1=50#整数
num2=3.14#浮点型
num3=1+2j#复数
num4=123e5#科学计数法
print(int(num4))#输出num4，num4的类型为浮点型
n=None#空类型
print(num1!=num2 or num2==num1)#输出判断结果#not优先级大于or和and

p="hello world"
#p=20#不同于VB，Python可以任意更改变量类型

s1=0O27#赋值任意一个八进制数
s2=0b100110100#二进制
s3=0xA21#十六进制
print(s1)
print(s2)
print(s3)#输出各个进制数
