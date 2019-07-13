di = [0,1,0,-1]
dj = [1,0,-1,0]
def dfs(i,j,n,s):
    for k in range(len(di)):
        dx = i + di[k]
        dy = j + dj[k]
        if 0 <= dx < 4 and 0 <= dy < 4:
            if n == 7:
                set_res.add(s)
            else:
                dfs(dx,dy,n+1,s*10+M[dx][dy])
 
 
for t in range(1, int(input())+1):
    M = [list(map(int, input().split())) for i in range(4)]
     
    set_res = set()
    for i in range(4):
        for j in range(4):
            dfs(i,j,1,M[i][j])
    print("#{} {}".format(t,len(set_res)))