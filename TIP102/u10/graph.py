class GraphNode:
    def __init__(self, value, edges = None):
        self.val = value
        if not edges:
            self.edges = []
        else:
            self.edges = edges
    
    def add_connection(self, new_node):
        self.edges.append(new_node)


List_of_Edges = [
    [0.1],
    [1,2],
    [2,3]
]

adjacency_list = [
    [1],
    [0,2],
    [1,3],
    [2]
]
adjacency_dictionary = {
    0: [1],
    1: [0,2],
    2: [1,3],
    3: [2]
}

adjacency_dictionary = {
    "Mexico City": ["São Paulo", "Los Angeles"],
    "Los Angeles": ["Mexico City", "Atlanta"],
    "Atlanta": ["Los Angeles"],
    "São Paulo": []
}

adjacency_dictionary = {
    "Mexico City": [("São Paulo", 200), ("Los Angeles", 110)],
    "Los Angeles": [("Mexico City", 300), ("Atlanta", 100)],
    "Atlanta": [("Los Angeles", 250)],
    "São Paulo": []
}

adjacency_matrix = [
    [0,1,0,0],
    [1,0,1,0],
    [0,1,0,1],
    [0,0,1,0]
]
# adjacency_matrix[i][j] = adjacency_matrix[j][i] 

BFS:
queue: 
initialize an empty list of visited nodes
initialize an empty queue
add the node we would like to start our traversal from to the queue
add the node we would to start out traversal from to visited
while the queue is not empty:
    remove an element from the queue and store it in a varibale, 'current'
    loop throught the neighbor has not yet been visited
        add the neighbor to the queue
        add the neighbor to the list of visited nodes
    
return the list of visited nodes

deapth-first search(dfs)
initialize an empty stack
initialize an empty list to store visited nodes
add the node we would like to start our traversal from to the stack
while the stack is not empty:
    pop the topmost node off the stack and store it in a variable, 'current'
    if the ndoe is already in the list of visited ndoes:
        add 'current' to the list of visited ndoes
    loop through the current node s neighbors
        if the neighobor has not yet been visited
            push the neighobor onto the stack
return list of visited nodes

dfs are usually recursively implemented with a helper function
main function
def dfs(self, start_node):
    create empty list to store nodes that have been visited
    pass list of visited ndoes and 'start ndoe' into 'dfs helper'
    return list of visited ndoes

helper function
def def_helper(self, start_node)
    if start node is not in list of visted nodes
    append start node to list of visted ndoes
    loop through start node neighbors
        call def helper passing list of visted nodes and the neighobr as the new start node

bfs is for shortest/least-cost path in an unweighted graph
also for searching a node that is likely to be close to the start node

dfs is use for cycle detection in directed graph by checking for back edges during traversal while bfs is for undirected
dfs is for backtracking problems
detecting cycles in graphs
topoligical sorting of DAG

graph representation BIG O
List of Edges:
    determinging if two nodes share an edge O(E) E is number of edges in the graph
    retrieving a Nodes neighbors: o(E)
    space complecity: O(E)

Adjacency lists
determining if two nodes share an edge, o(D) degree of the node, number of edges the node has
    worst case is O(N)
retriving a node neighbors: o(1) time to find all the neighbors of a particular node
space complexity: O(E)
    in the case of an undirected graph, each edge in the graph is stores twice

Adjacency matrix
determine if two nodes share an edge: o(1)
retrieving a node neighbors: O(N)
space complecity: O(N^2)

Bonus Syntax&Concepts
backtracking 
topological sorting
Dijkstra's algorithm finds the shortest path in a weighted graph
minimum spanning trees a subset of edges in an undirected, connected weighted graph inclueded all nodes in the graph while miniizing the total edge weighted
prim''s algorithm
kruskal's algorithm

Prim's Algorithm in python
INF = 999999
V = 5
G = [[0, 9, 75, 0, 0],
     [9, 0, 95, 19, 42],
     [75, 95, 0, 51, 66],
     [0, 19, 51, 0, 31],
     [0, 42, 66, 31, 0]]

selected = [0,0,0,0,0]

number_edge = 0

selected[0] = True

print('Edge: weight')
while (number_edge < V-1):
    minium = INF
    x = y = 0
    for in range(V):
        if ((not slected[j]) and G[i][j]) :
            if minimun > G[i][j]:
                minumium = G[i][j]
                x=i
                y=j
    print(str(x) + '-' str(y) + ':' + str(G[x][y]))
    selected[y] = True
    number_edge  += 1