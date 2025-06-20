t=int(input())
for _ in range(t):
    n=int(input())
    cells=input()
    continuous=False
    cnt=0
    for i in range(n):
        if cells[i]=='.' and i+1<n and cells[i+1]=='.' and i+2<n and cells[i+2]=='.':
            continuous=True
            break
        if cells[i]=='.':
            cnt+=1
    if continuous:
        print(2)
    else:
        print(cnt)