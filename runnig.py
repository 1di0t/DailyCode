direct = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def solution(maps):
    answer = 0

    max_y = len(maps)
    max_x = len(maps[0])
    visited = [[False] * max_x for _ in range(max_y)]
    queue = []
    queue.append((0, 0))
    visited[0][0] = True
    while queue:
        x, y = queue.pop(0)
        if x == max_x - 1 and y == max_y - 1:
            answer = maps[y][x]
            break
        for dx, dy in direct:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < max_x and 0 <= ny < max_y and not visited[ny][nx] and maps[ny][nx] == 1:
                visited[ny][nx] = True
                maps[ny][nx] = maps[y][x] + 1
                queue.append((nx, ny))
    if answer == 0:
        return -1
    return answer

print(solution(	[[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 1], [0, 0, 0, 0, 1]]))