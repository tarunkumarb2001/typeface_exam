n=int(input())
l=['1','2','5','6','8','9','10','0']
c=0
if n<8:
    print(int(l[n]))
else:
    check=[1,2,5,6,8,9,10]
    i=10
    while len(check)<=(n):
        k=list(str(i))
        if all(a in l for a in k):
            c=i
        check.append(i)
        i+=1
    print(c)