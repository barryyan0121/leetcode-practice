"""3493. 属性图"""


class Solution:
    def numberOfComponents(self, properties: list[list[int]], k: int) -> int:
        n = len(properties)
        parent = list(range(n))

        def find(x: int) -> int:
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        components = n
        property_sets = [set(values) for values in properties]
        for i in range(n):
            for j in range(i):
                if len(property_sets[i] & property_sets[j]) < k:
                    continue
                root_i, root_j = find(i), find(j)
                if root_i != root_j:
                    parent[root_i] = root_j
                    components -= 1
        return components


if __name__ == "__main__":
    test_cases = [
        (([[1, 2], [1, 1], [3, 4], [4, 5], [5, 6], [7, 7]], 1), 3),
        (([[1, 2, 3], [2, 3, 4], [4, 3, 5]], 2), 1),
        (([[1, 1], [1, 1]], 2), 2),
    ]
    for _, ((properties, k), expected) in enumerate(test_cases):
        assert Solution().numberOfComponents(properties, k) == expected
