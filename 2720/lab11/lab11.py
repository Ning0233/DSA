def dfs(graph, start):
    """
    Depth First Search (DFS) traversal of a graph.
    Parameters:
        graph (list of lists): Adjacency list representation of the graph.
        start (int): Starting node for traversal.
    Returns:
        list: Nodes in depth-first traversal order.
    """
    visited = set()
    result = []

    def dfs_helper(node):
        if node not in visited:
            visited.add(node)
            result.append(node)
            for neighbor in graph[node]:
                dfs_helper(neighbor)

    dfs_helper(start)
    return result


def bfs(graph, start):
    """
    Breadth First Search (BFS) traversal of a graph.
    Parameters:
        graph (list of lists): Adjacency list representation of the graph.
        start (int): Starting node for traversal.
    Returns:
        list: Nodes in breadth-first traversal order.
    """
    visited = set()
    queue = [start]
    result = []

    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.add(node)
            result.append(node)
            queue.extend(graph[node])

    return result