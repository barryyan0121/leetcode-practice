"""2101. 引爆最多的炸弹"""


class Solution:
    def maximumDetonation(self, bombs: list[list[int]]) -> int:
        graph = [[] for _ in bombs]
        for i, (x, y, radius) in enumerate(bombs):
            for j, (xx, yy, _) in enumerate(bombs):
                if i != j and (x - xx) ** 2 + (y - yy) ** 2 <= radius * radius:
                    graph[i].append(j)
        answer = 0
        for start in range(len(bombs)):
            seen = {start}
            stack = [start]
            while stack:
                for neighbor in graph[stack.pop()]:
                    if neighbor not in seen:
                        seen.add(neighbor)
                        stack.append(neighbor)
            answer = max(answer, len(seen))
        return answer


if __name__ == "__main__":
    test_cases = [(([[2, 1, 3], [6, 1, 4]],), 2)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().maximumDetonation(*args) == expected
