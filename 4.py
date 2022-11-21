l1=[]
for i in range(256):
    l1.append(list(map(int,input().split())))    
le,right,top,bottom=99999999,0,99999999,0
for i in range(256):
    for j in range(256):
        if l1[i][j]==0:
            le=min(le,i)
            right=max(right,j)
            top=min(top,j)
            bottom=max(bottom,i)
l2=[(le,top),(le,right),(bottom,top),(bottom,right)]
print(*l2)