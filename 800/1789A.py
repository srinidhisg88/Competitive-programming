from math import gcd
t=int(input())
for _ in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    flag=0
    for i in range(n):
        for j in range(i+1,n):
            if gcd(arr[i],arr[j])<=2:
                flag=1
    if flag==0:
        print('no')
    else:
        print('yes')