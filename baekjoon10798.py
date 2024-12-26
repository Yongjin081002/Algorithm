li = []
for i in range(5):
    li.append(input())

max_length = max(len(row) for row in li)

for index in range(max_length):
    for row in li:
        if index < len(row): 
            print(row[index], end='')
