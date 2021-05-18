list1=[1,2,3,5,7,12,19] #数字列表
list2=['strawberry','watermelon','mango'] #字符串列表
student=['55122005100','李明','男',19] #学生列表
print(student)
list4=[i for i in range(1,20,2)] #list4是1到19的奇数
print(list4)
#向列表中添加元素
list3=list1+list2 #列表合并（连接）
print(list3)
list1.append(31) #在list1中朝最后一个位置添加元素
print(list1)
list1.insert(1,2) #在list1中朝下标为1的位置添加元素2
print(list1)
#删除列表中的元素
list2.pop(2) #删除list2中下标为2的元素
list2.remove('watermelon') #去除list2中的'watermelon'元素
print(list2)
#del list2
print(list2)
#修改列表中的元素
student[2]='女'
print(student)
student[1:3]=['李华','男','18']
print(student)
student[1::]=['李丽'] #原列表未被取代的元素都会被删掉
print(student)
student[1::]=['李刚','男','20'] #多个元素会延长列表长度
print(student)
#取最大、最小值和平均值
#方法一：用max、min
print(max(list1))
print(min(list1))
#方法二：用循环实现
ma=list1[0]
mi=list1[0]
average=0
sum=0
for k in list1:
    if ma<k:
        ma=k
    if mi>k:
        mi=k
    sum+=k
average=sum/len(list1)
print(ma)
print(mi)
print(average)