class Solution:
    def minimumCost(self, n: int, connections: list[list[int]]) -> int:
        parent = list(range(n + 1))
        size = [1] * (n + 1)

        def find(city):
            while city != parent[city]:
                parent[city] = parent[parent[city]]
                city = parent[city]
            return city

        cost = edges = 0
        for first, second, price in sorted(
            connections, key=lambda connection: connection[2]
        ):
            first_root, second_root = find(first), find(second)
            if first_root == second_root:
                continue
            if size[first_root] < size[second_root]:
                first_root, second_root = second_root, first_root
            parent[second_root] = first_root
            size[first_root] += size[second_root]
            cost += price
            edges += 1
            if edges == n - 1:
                return cost
        return 0 if n == 1 else -1


if __name__ == "__main__":
    test_cases = [
        (3, [[1, 2, 5], [1, 3, 6], [2, 3, 1]], 6),
        (4, [[1, 2, 3], [3, 4, 4]], -1),
        (1, [], 0),
        (4, [[1, 2, 1], [2, 3, 2], [3, 4, 3], [1, 4, 10], [1, 3, 10]], 6),
    ]
    for _, (n, connections, expected) in enumerate(test_cases):
        assert Solution().minimumCost(n, connections) == expected
