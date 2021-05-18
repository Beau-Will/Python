#第一题
tp1=(10,20,55,90,20,10,20)
set1=set(tp1)
list1=list(set1)
list1.sort()
tp1=tuple(list1)
print(tp1)
#第二题
dict1={'王洪':90,'刘芸':60,'张天青':100,'胡源':70,'卢果':100}
maxvalues=max(dict1.values())
print('最高分数是'+str(maxvalues))
print('得到最高分的学生名是：',end='')
for i in dict1.keys():
    if dict1[i]==maxvalues:
        print(i,end=';')