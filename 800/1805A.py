t=int(input())
for _ in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    ## if n is even
    total_xor=0
    for a in arr:
        total_xor^=a
    if n%2==0:
        if total_xor==0:
            print(total_xor)
        else:
            print(-1)
    else:
        print(total_xor)