n = int(input())
a=[]
t=int(input())
a.append(t)
m=k=a[0]
t=j=0
for i in range(1,n):
    t=int(input())
    a.append(t)
    if a[i]>m:
        m=a[i]
        t=i
    if a[i]<k:
        k=a[i]
        j=i

a[t]=k
a[j]=m
print(a)
