def rats(r,u,n,a):
    if n==0:
        return -1
    tf=r*u
    f=0
    for i in range(n):
        f+=a[i]
        if f>=tf:
            break
        else:
            return 0
    return i+1

r=int(input())            
u=int(input())
n=int(input())
a=list(map(int,input().split()))
print(rats(r,u,n,a))