from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    # 1) 좌표 2배 확대 후 사용할 격자 크기 설정
    SIZE = 102
    field = [[-1] * SIZE for _ in range(SIZE)]

    # 2) 각 직사각형에 대해 경계만 1, 내부는 0으로 표시
    for (x1, y1, x2, y2) in rectangle:
        x1, y1, x2, y2 = x1*2, y1*2, x2*2, y2*2
        for i in range(x1, x2+1):
            for j in range(y1, y2+1):
                if x1 < i < x2 and y1 < j < y2:
                    field[i][j] = 0
                elif field[i][j] != 0:
                    field[i][j] = 1

    # 3) 시작점과 목표점을 2배 좌표로 변환
    start_x, start_y = characterX * 2, characterY * 2
    target_x, target_y = itemX * 2, itemY * 2

    # 4) BFS 초기화
    visited = [[False]*SIZE for _ in range(SIZE)]
    queue = deque([(start_x, start_y, 0)])  # (x, y, dist_in_doubled_grid)
    visited[start_x][start_y] = True

    # 5) BFS 탐색
    while queue:
        x, y, dist = queue.popleft()
        # 목표에 도달하면 실제 이동 칸 수를 계산하여 반환
        if x == target_x and y == target_y:
            # dist는 2배 확대된 격자에서의 이동 횟수이므로
            moves = dist // 2
            return moves

        # 상하좌우 4방향 탐색
        for dx, dy in [(0,1), (0,-1), (-1,0), (1,0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < SIZE and 0 <= ny < SIZE:
                if not visited[nx][ny] and field[nx][ny] == 1:
                    visited[nx][ny] = True
                    queue.append((nx, ny, dist+1))
    
    # 목표에 도달하지 못한 경우
    return -1
