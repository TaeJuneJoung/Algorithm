import sys
sys.stdin = open('../input/p3032.txt', 'r')

def ext_euclid(a, b):
	n = [a, b]
	x = [1, 0]
	y = [0, 1]
	while n[-1] != 0:
		d = n[-2] // n[-1]
		n.append(n[-2] - d * n[-1])
		x.append(x[-2] - d * x[-1])
		y.append(y[-2] - d * y[-1])
	return x[-2], y[-2]

res = []
for t in range(1, int(input())+1):
	a, b = map(int, input().split())
	x, y = ext_euclid(a,b)
	res.append(str(x)+" "+str(y))
	
for i in range(len(res)):
	print("#{} {}".format(i+1, res[i]))