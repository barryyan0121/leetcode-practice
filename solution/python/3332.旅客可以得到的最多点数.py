class Solution:
    def maxScore(
        self,
        n: int,
        k: int,
        stayScore: list[list[int]],
        travelScore: list[list[int]],
    ) -> int:
        scores = [0] * n
        for day in range(k):
            next_scores = [0] * n
            for destination in range(n):
                next_scores[destination] = (
                    scores[destination] + stayScore[day][destination]
                )
                for source in range(n):
                    if source != destination:
                        next_scores[destination] = max(
                            next_scores[destination],
                            scores[source] + travelScore[source][destination],
                        )
            scores = next_scores
        return max(scores)


if __name__ == "__main__":
    test_cases = [
        ((2, 1, [[2, 3]], [[0, 2], [1, 0]]), 3),
        ((3, 2, [[3, 4, 2], [2, 1, 2]], [[0, 2, 1], [2, 0, 4], [3, 2, 0]]), 8),
    ]
    for _, ((n, k, stay_score, travel_score), expected) in enumerate(test_cases):
        assert Solution().maxScore(n, k, stay_score, travel_score) == expected
