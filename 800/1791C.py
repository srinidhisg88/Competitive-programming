t=int(input())
for _ in range(t):
    n=int(input())
    st=input()
    
    l,r=0,n-1
    while l<=r and ((st[l]=='0' and st[r]=='1') or (st[l]=='1' and st[r]=='0')):
        l+=1
        r-=1
    print(r-l+1)
