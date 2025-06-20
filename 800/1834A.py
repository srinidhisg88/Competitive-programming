t=int(input())
for _ in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    n,p=0,0
    for e in arr:
        if e<0:
            n+=1
        else:
            p+=1
    cnt=0
    while n%2!=0 or p<n:
        cnt+=1
        p+=1
        n-=1
    print(cnt)
