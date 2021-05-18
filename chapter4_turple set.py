#第一题
list1=input('list1=').split(' ')
ch=max(list1,key=list1.count)
for a in range(len(list1)-1,-1,-1): #逆序找出现次数最多的元素，然后删除
    if list1[a]==ch:
        list1.pop(a)
print(list1)

#第二题
list01=[[1,2,3],[4,5,6],[7,8,9]] #可以往后拓展，输出也没问题
i=0
while i<=len(list01)-1:
    if i%2==0:
        print(list01[i])
    else:
        list02=list(reversed(list01[i]))
        print(list02)
    i+=1

#第三题
#循环（但不是换行输出的，也是二维列表）
a=[[1,2,3,4],[5,6,7,8],[9,10,11,12]]
for i in range(4):
	a.append([])
	for j in range(4):
		a[i].append(i*4+j+1)
a = [[i * 3 + j for j in range(1, 4)] for i in range(4)]
print(a)
