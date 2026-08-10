"""2242. 节点序列的最大得分"""


class Solution:
    def maximumScore(self, scores: list[int], edges: list[list[int]]) -> int:
        graph = [[] for _ in scores]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        for i in range(len(scores)):
            graph[i].sort(key=lambda node: scores[node], reverse=True)
            graph[i] = graph[i][:3]
        answer = -1
        for a, b in edges:
            for x in graph[a]:
                if x == b:
                    continue
                for y in graph[b]:
                    if y == a or y == x:
                        continue
                    answer = max(answer, scores[x] + scores[a] + scores[b] + scores[y])
        return answer
