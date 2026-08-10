"""2374. 节点拥有的最高边分数"""


class Solution:
    def edgeScore(self, edges: list[int]) -> int:
        scores = [0] * len(edges)
        for node, target in enumerate(edges):
            scores[target] += node
        return max(range(len(edges)), key=lambda node: (scores[node], -node))
