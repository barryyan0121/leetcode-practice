"""2049. 统计最高分的节点数目"""


class Solution:
    def countHighestScoreNodes(self, parents: list[int]) -> int:
        n = len(parents)
        children = [[] for _ in range(n)]
        for node in range(1, n):
            children[parents[node]].append(node)
        sizes = [0] * n
        scores = [0] * n

        def dfs(node: int) -> int:
            size = 1
            score = 1
            for child in children[node]:
                child_size = dfs(child)
                size += child_size
                score *= child_size
            if n - size:
                score *= n - size
            sizes[node] = size
            scores[node] = score
            return size

        dfs(0)
        maximum = max(scores)
        return scores.count(maximum)


if __name__ == "__main__":
    test_cases = [(([-1, 2, 0, 2, 0],), 3)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().countHighestScoreNodes(*args) == expected
