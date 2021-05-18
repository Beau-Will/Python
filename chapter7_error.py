class chaozhong(Exception):
    pass
try:
    height=int(input('身高='))
    weight=int(input('体重='))
    standard=height-100
    if height<30 or height>250:
        raise chaozhong
    else:
        if ((weight-standard)/standard)<=0.05 and ((weight-standard)/standard)>=-0.05:
            print('体重正常')
        elif ((weight-standard)/standard)>=0.05:
            print('体重超标')
        elif((weight-standard)/standard)<=-0.05:
            print('体重不达标')
except chaozhong as msg:
    print(msg)

#第二题
grades=int(input('请输入你的成绩='))
assert  grades<=100 and grades >=60,'?'
if grades>=90:
    print('成绩优秀')
elif grades>=80:
    print('成绩良好')
elif grades>=70:
    print('成绩中等')
else:
    print('成绩及格')
#第三题