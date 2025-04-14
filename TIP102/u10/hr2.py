def has_cycle(adj_matrix):
    visited = set()
    
    def dfs(i, parent, adj_matrix, visited):
        visited.add(i)
        for neighbor in range(len(adj_matrix)):
            if adj_matrix[i][neighbor] == 1:
                if neighbor not in visited:  # Visit unvisited neighbors
                    if dfs(neighbor, i, adj_matrix, visited):  # Recursive call with parent as i
                        return True
                elif neighbor != parent:  # If already visited and not parent, cycle detected
                    return True
        return False

    for i in range(len(adj_matrix)):
        if i not in visited:
            if dfs(i, -1, adj_matrix, visited):  # Start DFS from node i with no parent (-1)
                return True
    return False
