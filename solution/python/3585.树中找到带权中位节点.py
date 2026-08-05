"""3585. 树中找到带权中位节点"""


class Solution:
    def findMedian(
        self, n: int, edges: list[list[int]], queries: list[list[int]]
    ) -> list[int]:
        sabrelonta = queries
        graph = [[] for _ in range(n)]
        for first, second, weight in edges:
            graph[first].append((second, weight))
            graph[second].append((first, weight))
        parent = [0] * n
        depth = [0] * n
        distance = [0] * n
        order = [0]
        for node in order:
            for neighbor, weight in graph[node]:
                if neighbor != parent[node]:
                    parent[neighbor] = node
                    depth[neighbor] = depth[node] + 1
                    distance[neighbor] = distance[node] + weight
                    order.append(neighbor)
        levels = n.bit_length()
        up = [parent]
        for _ in range(1, levels):
            previous = up[-1]
            up.append([previous[previous[node]] for node in range(n)])

        def lca(first, second):
            if depth[first] < depth[second]:
                first, second = second, first
            difference = depth[first] - depth[second]
            bit = 0
            while difference:
                if difference & 1:
                    first = up[bit][first]
                difference >>= 1
                bit += 1
            if first == second:
                return first
            for bit in range(levels - 1, -1, -1):
                if up[bit][first] != up[bit][second]:
                    first, second = up[bit][first], up[bit][second]
            return parent[first]

        def climb_below(node, limit):
            used = 0
            for bit in range(levels - 1, -1, -1):
                ancestor = up[bit][node]
                jump = distance[node] - distance[ancestor]
                if used + jump < limit:
                    used += jump
                    node = ancestor
            return parent[node]

        def climb_within(node, limit):
            used = 0
            for bit in range(levels - 1, -1, -1):
                ancestor = up[bit][node]
                jump = distance[node] - distance[ancestor]
                if used + jump <= limit:
                    used += jump
                    node = ancestor
            return node

        answer = []
        for first, second in sabrelonta:
            common = lca(first, second)
            first_distance = distance[first] - distance[common]
            second_distance = distance[second] - distance[common]
            total = first_distance + second_distance
            if total == 0:
                answer.append(first)
                continue
            half = (total + 1) // 2
            if first_distance >= half:
                answer.append(climb_below(first, half))
            else:
                limit = second_distance - (half - first_distance)
                answer.append(climb_within(second, limit))
        return answer


if __name__ == "__main__":
    test_cases = [
        ((2, [[0, 1, 7]], [[1, 0], [0, 1]]), [0, 1]),
        ((3, [[0, 1, 2], [2, 0, 4]], [[0, 1], [2, 0], [1, 2]]), [1, 0, 2]),
        (
            (5, [[0, 1, 2], [0, 2, 5], [1, 3, 1], [2, 4, 3]], [[3, 4], [1, 2]]),
            [2, 2],
        ),
    ]
    for _, ((n, edges, queries), expected) in enumerate(test_cases):
        assert Solution().findMedian(n, edges, queries) == expected
