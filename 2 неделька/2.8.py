m = int(input())
M = list(map(int, input().split()))
n = 0
for i in range(0, m):
    for j in range(0, m):
        if M[i] > M[j]:
            n += 1
    if n == m//2:
        print(M[i])
        break