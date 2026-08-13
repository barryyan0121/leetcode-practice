"""2872. 可以被 K 整除连通块的最大数目"""


class Solution:
    def maxKDivisibleComponents(
        self, n: int, edges: list[list[int]], values: list[int], k: int
    ) -> int:
        graph = [[] for _ in range(n)]
        for left, right in edges:
            graph[left].append(right)
            graph[right].append(left)
        answer = 0

        def visit(node: int, parent: int) -> int:
            nonlocal answer
            total = values[node]
            for neighbor in graph[node]:
                if neighbor != parent:
                    total += visit(neighbor, node)
            if total % k == 0:
                answer += 1
                return 0
            return total

        visit(0, -1)
        return answer


if __name__ == "__main__":
    assert (
        Solution().maxKDivisibleComponents(
            5, [[0, 2], [1, 2], [1, 3], [2, 4]], [1, 8, 1, 4, 4], 6
        )
        == 2
    )
