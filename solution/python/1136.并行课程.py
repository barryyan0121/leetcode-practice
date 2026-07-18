from collections import deque


class Solution:
    def minimumSemesters(self, n: int, relations: list[list[int]]) -> int:
        graph = [[] for _ in range(n + 1)]
        indegree = [0] * (n + 1)
        for first, second in relations:
            graph[first].append(second)
            indegree[second] += 1
        queue = deque(course for course in range(1, n + 1) if not indegree[course])
        semesters = studied = 0
        while queue:
            semesters += 1
            for _ in range(len(queue)):
                course = queue.popleft()
                studied += 1
                for next_course in graph[course]:
                    indegree[next_course] -= 1
                    if not indegree[next_course]:
                        queue.append(next_course)
        return semesters if studied == n else -1


if __name__ == "__main__":
    test_cases = [
        (3, [[1, 3], [2, 3]], 2),
        (3, [[1, 2], [2, 3], [3, 1]], -1),
        (1, [], 1),
        (4, [[1, 2], [2, 3], [3, 4]], 4),
    ]
    for _, (n, relations, expected) in enumerate(test_cases):
        assert Solution().minimumSemesters(n, relations) == expected
