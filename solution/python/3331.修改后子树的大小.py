class Solution:
    def findSubtreeSizes(self, parent: list[int], s: str) -> list[int]:
        n = len(parent)
        original_children = [[] for _ in range(n)]
        for node in range(1, n):
            original_children[parent[node]].append(node)

        new_parent = parent[:]
        stack = [(0, False, [-1] * 26)]
        while stack:
            node, exiting, path = stack.pop()
            letter = ord(s[node]) - ord("a")
            if node != 0 and path[letter] != -1:
                new_parent[node] = path[letter]
            next_path = path[:]
            next_path[letter] = node
            for child in reversed(original_children[node]):
                stack.append((child, False, next_path))

        children = [[] for _ in range(n)]
        for node in range(1, n):
            children[new_parent[node]].append(node)
        order = [0]
        for node in order:
            order.extend(children[node])
        sizes = [1] * n
        for node in reversed(order[1:]):
            sizes[new_parent[node]] += sizes[node]
        return sizes


if __name__ == "__main__":
    test_cases = [
        (([-1, 0, 0, 1, 1, 1], "abaabc"), [6, 3, 1, 1, 1, 1]),
        (([-1, 0, 4, 0, 1], "abbba"), [5, 2, 1, 1, 1]),
    ]
    for _, ((parent, s), expected) in enumerate(test_cases):
        assert Solution().findSubtreeSizes(parent, s) == expected
