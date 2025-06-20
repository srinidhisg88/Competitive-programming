t = int(input())
score = [[1 + min(i, 9 - i, j, 9 - j) for j in range(10)] for i in range(10)]
for _ in range(t):
    # Read 5 rows of the grid
    
    a=[input() for _ in range(10)]
    su=0
    for i in range(10):
        for j in range(10):
            if a[i][j]=='X':
                su+=score[i][j]
    print(su)