"""1938. 查询最大基因差"""


class Solution:
    def maxGeneticDifference(
        self, parents: list[int], queries: list[list[int]]
    ) -> list[int]:
        children = [[] for _ in parents]
        root = 0
        for node, parent in enumerate(parents):
            if parent == -1:
                root = node
            else:
                children[parent].append(node)
        by_node = [[] for _ in parents]
        for index, (node, value) in enumerate(queries):
            by_node[node].append((index, value))
        answer = [0] * len(queries)
        trie = [0, {}]

        def add(value: int, delta: int) -> None:
            node = trie
            for bit in range(17, -1, -1):
                child = node[1].setdefault((value >> bit) & 1, [0, {}])
                child[0] += delta
                node = child

        def best(value: int) -> int:
            node = trie
            result = 0
            for bit in range(17, -1, -1):
                want = 1 - ((value >> bit) & 1)
                if want in node[1] and node[1][want][0] > 0:
                    result |= 1 << bit
                    node = node[1][want]
                else:
                    node = node[1][1 - want]
            return result

        def dfs(node: int) -> None:
            add(node, 1)
            for index, value in by_node[node]:
                answer[index] = best(value)
            for child in children[node]:
                dfs(child)
            add(node, -1)

        dfs(root)
        return answer


if __name__ == "__main__":
    test_cases = [(([-1, 0, 1, 1], [[0, 2], [3, 3]]), [2, 3])]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().maxGeneticDifference(*args) == expected
