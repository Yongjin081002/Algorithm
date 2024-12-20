# n = int(input())
# res = 0
# for i in range(1,n+1):
#     res = 0
#     for j in range(n):
#         print(i+res,end=' ')
#         res += n
#     print()

def nsum(n) :
	if n == 1:
		return 1
	return n + nsum(n-1)

n = int(input())
print(nsum(n))