

def solution(n, computers):
    answer = 0
    visited = [False] * n
    def dfs(node):
        visited[node] = True
        for i in range(n):
            if computers[node][i] == 1 and not visited[i]:
                dfs(i)
            
    for i in range(n):
        if not visited[i]:
            dfs(i)
            answer += 1

    return answer

print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]])) 