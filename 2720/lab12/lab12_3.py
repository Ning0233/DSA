def course_schedule(n, prerequisites):
    """
    Determines the order of courses to take based on prerequisites.
    Parameters:
        n (int): Number of courses.
        prerequisites (list of lists): List of prerequisite pairs [a, b], where b must be taken before a.
    Returns:
        list: A list of courses in topological order if possible, otherwise an empty list if a cycle exists.
    """
    # Create adjacency list
    adjList = {course: [] for course in range(n)}
    for edge in prerequisites:
        adjList[edge[1]].append(edge[0])

    for course in adjList:
        adjList[course].sort()
    visited = set()
    topological_sort = []
    cycle_test = False

    def dfs(start, state):
        nonlocal cycle_test
        if start in state:  # Detect cycle
            cycle_test = True
            return
        if start in visited:  # Skip already visited nodes
            return

        visited.add(start)
        state.add(start)

        for neighbor in adjList[start]:
            dfs(neighbor, state)

        topological_sort.append(start)
        state.remove(start)

    # Perform DFS for all courses
    for course in range(n):
        if course not in visited:
            dfs(course, set())

    return topological_sort[::-1] if not cycle_test else []


def test_course_schedule():
    test_cases = [
        # Test case 1
        {"n": 4, "prerequisites": [[1, 0], [2, 0]], "expected": [0, 1, 2, 3]},
        # Test case 2
        {"n": 5, "prerequisites": [[1, 0], [2, 0]], "expected": [0, 1, 2, 3, 4]},
        # Test case 3
        {"n": 5, "prerequisites": [[2, 0], [3, 1]], "expected": [0, 1, 2, 3, 4]},
        # Test case 4
        {"n": 6, "prerequisites": [[1, 0], [2, 0]], "expected": [0, 1, 2, 3, 5, 4]},
        # Test case 5 (Cycle)
        {"n": 2, "prerequisites": [[0, 1], [1, 0]], "expected": []},
        # Test case 6 (Cycle)
        {"n": 3, "prerequisites": [[0, 1], [1, 2], [2, 0]], "expected": []},
        # Test case 7 (Cycle)
        {"n": 4, "prerequisites": [[0, 1], [1, 0]], "expected": []},
        # Test case 8
        {"n": 5, "prerequisites": [[1, 0], [2, 1], [3, 1], [3, 2], [4, 2], [4, 3]], "expected": [0, 1, 2, 3, 4]},
        # Test case 9
        {"n": 4, "prerequisites": [[1, 0], [2, 1], [3, 2]], "expected": [0, 1, 2, 3]},
        # Test case 10
        {"n": 5, "prerequisites": [[1, 0], [2, 1], [3, 2], [4, 3]], "expected": [0, 1, 2, 3, 4]},
        # Test case 11
        {"n": 4, "prerequisites": [[2, 0], [2, 1], [3, 2]], "expected": [0, 1, 2, 3]},
        # Test case 12
        {"n": 6, "prerequisites": [[3, 0], [3, 1], [4, 1], [5, 2], [5, 3], [5, 4]], "expected": [0, 1, 2, 3, 4, 5]},
        # Test case 13
        {"n": 4, "prerequisites": [[1, 0], [2, 0], [3, 1], [3, 2]], "expected": [0, 1, 2, 3]},
        # Test case 14
        {"n": 5, "prerequisites": [[1, 0], [2, 0], [3, 1], [4, 1], [4, 2]], "expected": [0, 1, 2, 3, 4]},
    ]

    for i, test in enumerate(test_cases):
        result = course_schedule(test["n"], test["prerequisites"])
        assert result == test["expected"], f"Test case {i + 1} failed: expected {test['expected']}, got {result}"
    print("All test cases passed!")


# Run the tests
test_course_schedule()