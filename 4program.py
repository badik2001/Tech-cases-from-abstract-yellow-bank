n, dir = input().split()
n = int(n)
a = [[int(x) for x in input().split()] for _ in range(n)]

if dir == 'R':
    for i in range(n // 2):
        for j in range(n):
            a[i][j], a[n - 1 - i][n - 1 - j] = a[n - 1 - i][n - 1 - j], a[i][j]
    for i in range(n):
        for j in range(i):
            a[i][j], a[j][i] = a[j][i], a[i][j]
else:
    for i in range(n // 2):
        for j in range(n):
            a[i][j], a[n - 1 - i][j] = a[n - 1 - i][j], a[i][j]
    for i in range(n):
        for j in range(i):
            a[i][j], a[j][i] = a[j][i], a[i][j]

k = 0
for i in range(n):
    for j in range(i):
        k += 1

print(k)
for i in range(n):
    for j in range(i):
        print(i, j, j, i)