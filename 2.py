str1,str2=map(str,input().split(","))
if str1=='' or str2=='':
    print(0)
else:        
    a=str2[-1]
    count=0
    for i in str1:
        if i==a:
            count+=1
    print(count)
