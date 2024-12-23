a = list(map(int, input()))
count = 0
sum_a = sum(a)

while sum_a >= 10:
    count += 1
    temp_sum = 0
    while sum_a > 0:
        temp_sum += sum_a % 10 
        sum_a //= 10          
    sum_a = temp_sum 


if sum_a % 3 == 0:
    print(count + 1)  
    print('YES')
else:
    print(count + 1) 
    print('NO')
