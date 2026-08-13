from typing import List


class Solution:
    def palindromePath(
        self, n: int, edges: List[List[int]], s: str, queries: List[str]
    ) -> List[bool]:
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        log = n.bit_length()
        up = [[0] * n for _ in range(log)]
        depth = [0] * n
        tin, tout, order = [0] * n, [0] * n, []
        stack = [(0, 0, 0)]
        while stack:
            node, parent, state = stack.pop()
            if state == 0:
                up[0][node] = parent
                tin[node] = len(order)
                order.append(node)
                stack.append((node, parent, 1))
                for child in reversed(graph[node]):
                    if child != parent:
                        depth[child] = depth[node] + 1
                        stack.append((child, node, 0))
            else:
                tout[node] = len(order) - 1
        for j in range(1, log):
            for node in range(n):
                up[j][node] = up[j - 1][up[j - 1][node]]

        def lca(a, b):
            if depth[a] < depth[b]:
                a, b = b, a
            diff = depth[a] - depth[b]
            for j in range(log):
                if diff >> j & 1:
                    a = up[j][a]
            if a == b:
                return a
            for j in range(log - 1, -1, -1):
                if up[j][a] != up[j][b]:
                    a, b = up[j][a], up[j][b]
            return up[0][a]

        bit = [0] * (n + 2)

        def add(index, value):
            index += 1
            while index <= n + 1:
                bit[index] ^= value
                index += index & -index

        def range_xor(left, right, value):
            add(left, value)
            add(right + 1, value)

        def point(index):
            index += 1
            value = 0
            while index:
                value ^= bit[index]
                index -= index & -index
            return value

        masks = [1 << (ord(char) - 97) for char in s]
        root_xor = [0] * n
        for node in order:
            root_xor[node] = root_xor[up[0][node]] ^ masks[node]

        answer = []
        for query in queries:
            parts = query.split()
            if parts[0] == "update":
                node, char = int(parts[1]), parts[2]
                value = masks[node] ^ (1 << (ord(char) - 97))
                masks[node] ^= value
                range_xor(tin[node], tout[node], value)
            else:
                a, b = map(int, parts[1:])
                common = lca(a, b)
                value = (
                    root_xor[a]
                    ^ point(tin[a])
                    ^ root_xor[b]
                    ^ point(tin[b])
                    ^ masks[common]
                    ^ point(tin[common])
                )
                answer.append(value & (value - 1) == 0)
        return answer


if __name__ == "__main__":
    solution = Solution()
    assert solution.palindromePath(
        3, [[0, 1], [1, 2]], "aac", ["query 0 2", "update 1 b", "query 0 2"]
    ) == [True, False]
