class Solution:
    def mostSimilar(
        self, n: int, roads: list[list[int]], names: list[str], targetPath: list[str]
    ) -> list[int]:
        graph = [[] for _ in range(n)]
        for a, b in roads:
            graph[a].append(b)
            graph[b].append(a)

        length = len(targetPath)
        dp = [[length] * n for _ in range(length)]
        parent = [[-1] * n for _ in range(length)]
        for city in range(n):
            dp[0][city] = names[city] != targetPath[0]
        for index in range(1, length):
            for city in range(n):
                previous = min(
                    graph[city], key=lambda neighbor: dp[index - 1][neighbor]
                )
                dp[index][city] = dp[index - 1][previous] + (
                    names[city] != targetPath[index]
                )
                parent[index][city] = previous

        city = min(range(n), key=lambda node: dp[-1][node])
        path = [city]
        for index in range(length - 1, 0, -1):
            city = parent[index][city]
            path.append(city)
        return path[::-1]


if __name__ == "__main__":
    test_cases = [
        (
            5,
            [[0, 2], [0, 3], [1, 2], [1, 3], [1, 4], [2, 4]],
            ["ATL", "PEK", "LAX", "DXB", "HND"],
            ["ATL", "DXB", "HND", "LAX"],
            1,
        )
    ]
    for _, (n, roads, names, target, expected) in enumerate(test_cases):
        path = Solution().mostSimilar(n, roads, names, target)
        assert all(
            path[index + 1]
            in {a if b == path[index] else b for a, b in roads if path[index] in (a, b)}
            for index in range(len(path) - 1)
        )
        assert sum(names[city] != name for city, name in zip(path, target)) == expected
