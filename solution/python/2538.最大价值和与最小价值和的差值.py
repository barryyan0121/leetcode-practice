"""2538. 最大价值和与最小价值和的差值"""


class Solution:
    def maxOutput(self, n: int, edges: list[list[int]], price: list[int]) -> int:
        graph = [[] for _ in range(n)]
        for first, second in edges:
            graph[first].append(second)
            graph[second].append(first)
        answer = 0

        def dfs(node: int, parent: int) -> tuple[int, int]:
            nonlocal answer
            best_full = best_without_leaf = 0
            has_child = False
            for child in graph[node]:
                if child == parent:
                    continue
                has_child = True
                child_full, child_without_leaf = dfs(child, node)
                through_previous = (
                    best_without_leaf + child_full + price[node]
                    if best_full or best_without_leaf
                    else child_without_leaf + price[node]
                )
                answer = max(
                    answer,
                    best_full + child_without_leaf + price[node],
                    through_previous,
                    child_full,
                )
                best_full = max(best_full, child_full)
                best_without_leaf = max(best_without_leaf, child_without_leaf)
            if not has_child:
                return price[node], 0
            return price[node] + best_full, price[node] + best_without_leaf

        dfs(0, -1)
        return answer


if __name__ == "__main__":
    test_cases = [
        ((6, [[0, 1], [1, 2], [1, 3], [3, 4], [3, 5]], [9, 8, 7, 6, 10, 5]), 24)
    ]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().maxOutput(*args) == expected
