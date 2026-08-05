"""2049. 统计最高分的节点数目"""


class Solution:
    def countHighestScoreNodes(self, parents: list[int]) -> int:
        n = len(parents)
        children = [[] for _ in parents]
        for node in range(1, n):
            children[parents[node]].append(node)
        size_cache = [0] * n

        def calc(node: int) -> int:
            total = 1
            for child in children[node]:
                total += calc(child)
            size_cache[node] = total
            return total

        calc(0)
        scores = [0] * n
        for node in range(n):
            score = max(1, n - size_cache[node])
            for child in children[node]:
                score *= size_cache[child]
            scores[node] = score
        return scores.count(max(scores))


if __name__ == "__main__":
    test_cases = [(([-1, 2, 0, 2, 0],), 3)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().countHighestScoreNodes(*args) == expected
