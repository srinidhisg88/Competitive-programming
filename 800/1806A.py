t=int(input())
for _ in range(t):
    sx,sy,dx,dy=map(int,input().split())
    if dy<sy:
        print(-1)
        continue
    moves=dy-sy
    sx+=moves
    if sx<dx:
        print(-1)
        continue
    moves+=(sx-dx)
    print(moves)