t=int(input())

for i in range(t):
    k = 1
    w_n = 0
    n = int(input())

    for j in range(1,n+1):
        num1 = j * ((k+1)*(k+2)/2)
        w_n += num1
        k += 1 

    print(int(w_n))