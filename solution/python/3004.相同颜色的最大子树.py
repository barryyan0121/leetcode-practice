class Solution:
    def maxSubtreeSize(self, edges: list[list[int]], colors: list[int]) -> int:
        n = len(colors)
        graph = [[] for _ in range(n)]
        for first, second in edges:
            graph[first].append(second)
            graph[second].append(first)
        answer = 0

        def dfs(node: int, parent: int) -> tuple[int, int]:
            nonlocal answer
            size = 1
            same = True
            for child in graph[node]:
                if child != parent:
                    child_size, child_color = dfs(child, node)
                    size += child_size
                    same &= child_color == colors[node]
            if same:
                answer = max(answer, size)
            return size, colors[node] if same else -1

        dfs(0, -1)
        return answer


if __name__ == "__main__":
    solution = Solution()
    assert solution.maxSubtreeSize([[0, 1], [0, 2], [0, 3]], [1, 1, 2, 3]) == 1
    assert solution.maxSubtreeSize([[0, 1], [0, 2], [0, 3]], [1, 1, 1, 1]) == 4
    assert (
        solution.maxSubtreeSize([[0, 1], [0, 2], [2, 3], [2, 4]], [1, 2, 3, 3, 3]) == 3
    )
