"""
DFS와 BFS에 대해 학습 중
아직 풀지 못함.
"""

N, M, start = map(int, input().split())
matrix = [[0] * (N+1) for i in range(N+1)]
for i in range(M):
    link = list(map(int, input().split()))
    matrix[link[0]][link[1]] = 1
    matrix[link[1]][link[0]] = 1

def dfs(start, row, foot_print):
    foot_print += [start]
    for search_node in range(len(row[start])):
        if row[start][search_node] and search_node not in foot_print:
            foot_print = dfs(search_node, row, foot_print)
    return foot_print

"""
dfs를 공부하기 위해 참고 사이트
https://this-programmer.com/entry/%EB%B0%B1%EC%A4%801260%ED%8C%8C%EC%9D%B4%EC%8D%AC-DFS%EC%99%80-BFS
"""