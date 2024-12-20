
r,g,b, = map(int,input().split())
for i in range(r):
    for j in range(g):
        for f in range(b):
            print(i,j,f)
print(r*g*b)