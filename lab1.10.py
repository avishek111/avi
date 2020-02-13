second=int(input("Enter the time in seconds: "))
p=second%86400
q=p%3600
r=q%60
if second>=86400:
    print('The time is:',second//86400,'days',p//3600,'Hours',q//60,'Minutes',r,'Seconds')
elif second<86400:
    print('The time is', p// 3600, 'Hours', p // 60, 'Minutes', r, 'Seconds')
