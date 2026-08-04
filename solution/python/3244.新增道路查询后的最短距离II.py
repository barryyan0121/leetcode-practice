class Solution:
    def shortestDistanceAfterQueries(
        self, n: int, queries: list[list[int]]
    ) -> list[int]:
        next_city = list(range(n + 1))

        def find(city: int) -> int:
            while next_city[city] != city:
                next_city[city] = next_city[next_city[city]]
                city = next_city[city]
            return city

        distance = n - 1
        answer = []
        for start, end in queries:
            city = find(start + 1)
            while city < end:
                next_city[city] = find(city + 1)
                city = find(city)
                distance -= 1
            answer.append(distance)
        return answer


if __name__ == "__main__":
    test_cases = [
        ((5, [[2, 4], [0, 2], [0, 4]]), [3, 2, 1]),
        ((4, [[0, 3], [0, 2]]), [1, 1]),
    ]
    for _, ((n, queries), expected) in enumerate(test_cases):
        assert Solution().shortestDistanceAfterQueries(n, queries) == expected
