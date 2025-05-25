t = int(input())
for _ in range(t):
    a, b, c = map(int, input().split())
    
    first_score = a + (c + 1) // 2
    second_score = b + c // 2

    if first_score > second_score:
        print('First')
    else:
        print('Second')