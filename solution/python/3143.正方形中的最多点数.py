class Solution:
    def maxPointsInsideSquare(self, points: list[list[int]], s: str) -> int:
        closest = [[10**20, 10**20] for _ in range(26)]
        distances = []
        for (x, y), character in zip(points, s):
            distance = max(abs(x), abs(y))
            distances.append(distance)
            pair = closest[ord(character) - ord("a")]
            if distance < pair[0]:
                pair[1] = pair[0]
                pair[0] = distance
            elif distance < pair[1]:
                pair[1] = distance

        limit = min(pair[1] for pair in closest)
        return sum(distance < limit for distance in distances)


if __name__ == "__main__":
    test_cases = [
        ([[1, 1], [-2, -2], [-2, 2]], "abb", 1),
        ([[1, 1], [-1, -1], [2, -2]], "ccd", 0),
    ]
    for _, (points, s, expected) in enumerate(test_cases):
        assert Solution().maxPointsInsideSquare(points, s) == expected
