class Solution:
    def __init__(self):
        self.cycle_test = False

    def course_schedule(self, n, prerequisites):
        adjList = {}
        for course in range(n):
            adjList[course] = []
        for edge in prerequisites:
            adjList[edge[1]] += [edge[0]]
        
        #print(adjList)
        
        visited = set()
        topological_sort = []
        
        
        def dfs(start, visited, adjList, state):
            print(state)
            if start in state: 
                self.cycle_test = True
                print("cycle_test")
                return

            if start in visited: 
                return

            visited.add(start)
            state.add(start)

            for neighbor in adjList.get(start,[]):
                dfs(neighbor, visited, adjList, state)            
            topological_sort.append(start)
            state.remove(start)

        for course in adjList: 
            dfs(course, visited, adjList, set())
        return(topological_sort[::-1]) if not self.cycle_test else []
