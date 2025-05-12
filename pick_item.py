def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0

    # Draw the rectangles on a 2D grid
    # grid = draw_rectangle(rectangle)
    print()
    draw_rectangle(rectangle)
    return answer

def draw_rectangle(rectangle):
    border, inside = "O", "X"

    # Draw the rectangles on a 2D grid
    max_x = max([rect[2] for rect in rectangle])+1
    max_y = max([rect[3] for rect in rectangle])+1
    grid = [[" "] * max_x for _ in range(max_y)]
    
    for rect in rectangle:
        x1, y1, x2, y2 = rect
        for i in range(x1, x2+1):
            for j in range(y1, y2+1):
                if i == x1 or i == x2 or j == y1 or j == y2:
                    # Mark the border of the rectangle
                    if grid[j][i] != inside:
                        grid[j][i] = border
                else:
                    # Mark the inside of the rectangle
                    grid[j][i] = inside
        

        for x in grid:
            print(x) 
    return grid


print(solution([[1,1,7,4],[3,2,5,5],[4,3,6,9],[2,6,8,8]],1,	3,7,8))