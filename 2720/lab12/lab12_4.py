from collections import deque, defaultdict

def course_schedule(n, prerequisites):
    # Create an adjacency list and in-degree array
    adj_list = defaultdict(list)
    in_degree = [0] * n

    # Build the graph
    for course, prereq in prerequisites:
        adj_list[prereq].append(course)
        in_degree[course] += 1

    # Initialize a queue with all courses having in-degree 0
    queue = deque([i for i in range(n) if in_degree[i] == 0])
    order = []

    # Process the courses
    while queue:
        current = queue.popleft()
        order.append(current)

        # Reduce the in-degree of neighboring courses
        for neighbor in adj_list[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # If the order contains all courses, return it; otherwise, return an empty list
    return order if len(order) == n else []

# Example usage
n = 4
prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]
print(course_schedule(n, prerequisites))  # Output: [0, 1, 2, 3]