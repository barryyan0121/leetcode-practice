"""2479. 两个不重叠子树的最大异或值"""


class Solution:
    def maxXor(self, n: int, edges: list[list[int]], values: list[int]) -> int:
        graph = [[] for _ in range(n)]
        for first, second in edges:
            graph[first].append(second)
            graph[second].append(first)

        parent = [-1] * n
        tin = [0] * n
        tout = [0] * n
        order = []
        stack = [(0, -1, 0)]
        time = 0
        while stack:
            node, previous, state = stack.pop()
            if state == 0:
                parent[node] = previous
                tin[node] = time
                time += 1
                order.append(node)
                stack.append((node, previous, 1))
                for neighbor in reversed(graph[node]):
                    if neighbor != previous:
                        stack.append((neighbor, node, 0))
            else:
                tout[node] = time - 1

        sums = values[:]
        for node in reversed(order[1:]):
            sums[parent[node]] += sums[node]

        left = [-1]
        right = [-1]

        def insert(value: int) -> None:
            node = 0
            for bit in range(60, -1, -1):
                branch = (value >> bit) & 1
                children = right if branch else left
                if children[node] == -1:
                    children[node] = len(left)
                    left.append(-1)
                    right.append(-1)
                node = children[node]

        def best(value: int) -> int:
            node = 0
            result = 0
            for bit in range(60, -1, -1):
                branch = (value >> bit) & 1
                preferred = left if branch else right
                fallback = right if branch else left
                if preferred[node] != -1:
                    result |= 1 << bit
                    node = preferred[node]
                else:
                    node = fallback[node]
            return result

        by_end = sorted(range(n), key=tout.__getitem__)
        by_start = sorted(range(n), key=tin.__getitem__)
        end_index = answer = 0
        for node in by_start:
            while end_index < n and tout[by_end[end_index]] < tin[node]:
                insert(sums[by_end[end_index]])
                end_index += 1
            if end_index:
                answer = max(answer, best(sums[node]))
        return answer


if __name__ == "__main__":
    test_cases = [
        ((6, [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5]], [2, 8, 3, 6, 2, 5]), 24)
    ]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().maxXor(*args) == expected
