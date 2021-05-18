#第一题
'''
f=open('f:/rand_25.txt','w')
import random
for i in range(1,101):
    f.write(str(random.randint(0,9)))
    f.write(' ')
    if i%10==0:
        f.write('\n')
f.close()
with open('f:/rand_25.txt','r+')as f:
    for j in range(1, 11):
        f.write('0')
        f.write(' ')
    f.write('\n')
with open('f:/rand_25.txt','a+')as f:
    for k in range(1, 11):
        f.write('1')
        f.write(' ')
#第二题
ls=[90,89,100,68,76,93,55,80]
import json
with open('f:/python课程成绩.txt','w')as f2:
    json.dump(ls,f2)
with open('f:/python课程成绩.txt','r')as fr2:
    newls=json.load(fr2)
    print(newls)
    sum=0
    for i in range(len(newls)):
        sum+=newls[i]
    ave=sum/len(newls)
    print(ave)
#第三题
with open('f:/test_25.txt','w')as f3:
    f3.write('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')#输入字符串
with open('f:/test_25.txt','r')as fr3:
    str_3=fr3.read()
    print(str_3)#取出并打印字符串
newstr=''
for a in str_3:#用循环处理字符串
    if 'a'<=a<='y'or'A'<=a<='Y':
        a=str(chr(ord(a)+1))
    elif a=='z'or a=='Z':
        a=str(chr(ord(a)-25))
    newstr=newstr+a
print(newstr)
ff3=open('f:/test_25密文.txt','w')#创建密文文件
ff3.write(newstr)
'''
#第四题
import os
def mkdir(path):
    folder = os.path.exists(path)
    if not folder:  # 判断是否存在文件夹如果不存在则创建为文件夹
        os.makedirs(path)  # makedirs 创建文件时如果路径不存在会创建这个路径
file = "f:\\lg"
mkdir(file)  # 调用函数
q=os.chdir('f:\\lg')
for i in range(1,51):
    f4='%d.txt'% i
    with open(f4,'w')as ff4:
        ff4.write(str(i))
#删除

