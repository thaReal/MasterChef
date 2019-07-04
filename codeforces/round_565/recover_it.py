#!/usr/bin/python

N = 3 * 1000 * 1000 + 13

def sieve(lst, num):
	for i in range(N):
		lst[i] = i
	
	for i in range(2, N):
		if lst[i] != i:
			lst[i] = i / lst[i]
			continue
		
		j = pow(i, 2)
		while j < N:
			lst[j] = min(lst[j], i)
			j += i
	
	cur = 1
	for i in range(2, N):
		if lst[i] == i:
			num[i] = cur
			cur += 1
			
	return lst, num


# Main solver function
def recover_it(n, data):
	lst0 = [0 for i in range(N)]
	num0 = [0 for i in range(N)]
	lst, num = sieve(lst0, num0)
	
	cnt = [0 for x in range(N)]
	res = list()
	for i in data:
		cnt[i] += 1
	
	for i in range(N - 1, 0, -1):
		while cnt[i] > 0:
			if lst[i] == i:
				cnt[num[i]] -= 1
				res.append(num[i])
			else:
				cnt[lst[i]] -= 1
				res.append(i)
			cnt[i] -= 1
	
	a_str = [str(x) for x in res]
	return a_str
			

# Main
n = int(raw_input())
raw_data = raw_input().split(" ")
data = [int(x) for x in raw_data]
solution = " ".join(recover_it(n, data))
print solution
