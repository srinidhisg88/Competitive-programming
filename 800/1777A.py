t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    ans=0
    for i in range(0,n-1):
        if a[i]%2==a[i+1]%2:
            ans+=1
    print(ans)