a,b = map(int,input().split())
temp = (a*b)-(b-1)
end = a*b
for i in range(a):
    for j in range(temp,end+1):
        print(j,end=' ')
    temp -= b
    end -= b
    print()
