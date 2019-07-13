import sys
sys.stdin = open('../input/p4869.txt', 'r')

T = int(input())
res = []
for t in range(1,T+1):
    N = int(input())
    idx = N//10
    paper = [1,3,5]
    for i in range(3,idx):
        if i % 2 == 1:
            paper.append(paper[i-1]*2 +1)
        else:
            paper.append(paper[i-1]*2 -1)
    res.append(paper[idx-1])
for i in range(len(res)):
    print(f"#{i+1} {res[i]}")