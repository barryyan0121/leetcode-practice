from typing import List


class Solution:
    def interactionCosts(self, n: int, edges: List[List[int]], group: List[int]) -> int:
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        total = {}
        for x in group:
            total[x] = total.get(x, 0) + 1
        parent = [-1] * n
        order = [0]
        for u in order:
            for v in graph[u]:
                if v != parent[u]:
                    parent[v] = u
                    order.append(v)
        count = [{} for _ in range(n)]
        ans = 0
        for u in reversed(order):
            d = count[u]
            d[group[u]] = d.get(group[u], 0) + 1
            if parent[u] >= 0:
                for x, c in d.items():
                    ans += c * (total[x] - c)
                for x, c in d.items():
                    p = count[parent[u]]
                    p[x] = p.get(x, 0) + c
        return ans


if __name__ == "__main__":
    assert Solution().interactionCosts(3, [[0, 1], [1, 2]], [1, 1, 1]) == 4
