a,b = map(int,input().split())
temp = a*b
for i in range(a):
    for j in range(b):
        print(temp,end=' ')
        temp -= 1
    print()