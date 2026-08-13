from typing import List


class Solution:
    def minimumFlips(
        self, n: int, edges: List[List[int]], start: str, target: str
    ) -> List[int]:
        graph = [[] for _ in range(n)]
        for index, (u, v) in enumerate(edges):
            graph[u].append((v, index))
            graph[v].append((u, index))
        answer = []
        parent = [-1] * n
        order = [0]
        for u in order:
            for v, _ in graph[u]:
                if v != parent[u]:
                    parent[v] = u
                    order.append(v)
        state = [int(c) for c in start]
        wanted = [int(c) for c in target]
        for u in reversed(order[1:]):
            if state[u] != wanted[u]:
                for v, index in graph[u]:
                    if v == parent[u]:
                        answer.append(index)
                        break
                state[u] ^= 1
                p = parent[u]
                state[p] ^= 1
        if state[0] != wanted[0]:
            return [-1]
        return sorted(answer)


if __name__ == "__main__":
    s = Solution()
    assert s.minimumFlips(3, [[0, 1], [1, 2]], "010", "100") == [0]
    assert s.minimumFlips(2, [[0, 1]], "00", "01") == [-1]
