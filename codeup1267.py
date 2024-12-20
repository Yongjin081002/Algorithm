n = int(input())
a = list(map(int,input().split()))
sum = 0
for i in range(len(a)):
    if a[i]%5==1:
        sum += 1
print(sum)