"""2421. 好路径的数目"""


class Solution:
    def numberOfGoodPaths(self, vals: list[int], edges: list[list[int]]) -> int:
        parent = list(range(len(vals)))
        size = [1] * len(vals)

        def find(node: int) -> int:
            while parent[node] != node:
                parent[node] = parent[parent[node]]
                node = parent[node]
            return node

        def union(first: int, second: int) -> None:
            first, second = find(first), find(second)
            if first == second:
                return
            if size[first] < size[second]:
                first, second = second, first
            parent[second] = first
            size[first] += size[second]

        ordered_edges = sorted(
            edges, key=lambda edge: max(vals[edge[0]], vals[edge[1]])
        )
        nodes = sorted(range(len(vals)), key=vals.__getitem__)
        answer = 0
        edge_index = 0
        node_index = 0
        while node_index < len(nodes):
            value = vals[nodes[node_index]]
            while edge_index < len(ordered_edges):
                first, second = ordered_edges[edge_index]
                if max(vals[first], vals[second]) > value:
                    break
                union(first, second)
                edge_index += 1
            counts = {}
            while node_index < len(nodes) and vals[nodes[node_index]] == value:
                root = find(nodes[node_index])
                counts[root] = counts.get(root, 0) + 1
                node_index += 1
            answer += sum(count * (count + 1) // 2 for count in counts.values())
        return answer


if __name__ == "__main__":
    test_cases = [
        (
            (
                [1, 3, 2, 1, 3],
                [[0, 1], [0, 2], [2, 3], [2, 4]],
            ),
            6,
        )
    ]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().numberOfGoodPaths(*args) == expected
