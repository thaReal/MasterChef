import itertools

def convert_to_int(stack):
	new_stack = [int(x) for x in stack]
	return new_stack


def first_pass(stack):
	new_stack = list()
	cnt = 0
	for n in stack:
		if n % 3 != 0:
			new_stack.append(n)
		else:
			cnt += 1
	return new_stack, cnt


def try_merge(stack):
	r = 2
	c = itertools.combinations(stack, r)
	cnt = 0
	while r <= 3:
		try:
			num = 0
			val = c.next()
			for i in val:
				num += i
			if num % 3 == 0:
				for i in val:
					index = stack.index(i)
					stack.pop(index)
				cnt += 1
				c = itertools.combinations(stack, r)
		except:
			r += 1
			c = itertools.combinations(stack, r)
	return cnt


def merge_it(test):
	finished = False
	stack, cnt = first_pass(test)
	if len(stack) > 1:
		cnt += try_merge(stack)
	return cnt
		
	
# Main
n = int(raw_input())
for i in range(n):
	queries = int(raw_input())
	raw_test = raw_input().split(" ")
	test = convert_to_int(raw_test)
	solution = str(merge_it(test))
	print solution
