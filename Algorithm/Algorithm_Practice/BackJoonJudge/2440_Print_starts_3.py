n = int(input())
for i in range(n):
    tmp = ''
    for j in range(n-i):
        tmp += '*'
    print(tmp)