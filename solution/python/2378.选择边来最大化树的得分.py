"""2378. 选择边来最大化树的得分"""


class Solution:
    def maxScore(self, edges: list[list[int]]) -> int:
        children = [[] for _ in edges]
        for node in range(1, len(edges)):
            parent, weight = edges[node]
            children[parent].append((node, weight))

        def dfs(node: int) -> tuple[int, int]:
            blocked = 0
            best_gain = 0
            for child, weight in children[node]:
                child_free, child_blocked = dfs(child)
                blocked += child_free
                best_gain = max(best_gain, child_blocked + weight - child_free)
            return blocked + best_gain, blocked

        return dfs(0)[0]
