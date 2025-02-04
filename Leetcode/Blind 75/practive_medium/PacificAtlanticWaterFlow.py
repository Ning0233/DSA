class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])

        pacific_visited = set()
        altantic_visited = set()

        def dfs(visited, row, col, start_value):
            
            #check grid boundaries
            if row < 0 or row >= rows or col < 0 or col >= cols: return
            #cell has been visited
            if (row, col) in visited: return
            #check condition
            if heights[row][col] < start_value: return

            visited.add((row, col))

            #check 4 directions
            dfs(visited, row + 1, col, heights[row][col])
            dfs(visited, row - 1, col, heights[row][col])
            dfs(visited, row, col + 1, heights[row][col])
            dfs(visited, row, col - 1, heights[row][col])

        for col in range(cols):
            dfs(pacific_visited, 0, col, heights[0][col])
            dfs(altantic_visited, rows - 1, col, heights[rows - 1][col])
        for row in range(rows):
            dfs(pacific_visited, row, 0, heights[row][0])
            dfs(altantic_visited, row, cols -1, heights[row][col - 1])
        
        output = [list(cell) for cell in pacific_visited & altantic_visited]

        return output



"""
def dfs(matrix, x, y):
    # base condition: check if out of bounds or cell is water
    if x < 0 or x>= len(matrix) or y < 0 or y >= len(matrix[0]) or matrix[x][y] == 0: return

    # marik the current cell as visited
    matrix[x][y] = 0

    #move in all 4 directions

    dfs(matrix, x + 1, y)
    dfs(matrix, x - 1, y)
    dfs(matrix, x, y + 1)
    dfs(matrix, x, y - 1)
    
def countIslands(matrix):
    island_count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 1:
                island_count += 1
                dfs(matrix, i, j)
    
    return island_count
"""