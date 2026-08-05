class Solution:
    def minCosts(self, cost: list[int]) -> list[int]:
        minimum = cost[0]
        answer = [minimum]
        for value in cost[1:]:
            minimum = min(minimum, value)
            answer.append(minimum)
        return answer


if __name__ == "__main__":
    test_cases = [
        (([5, 3, 4, 1, 3, 2],), [5, 3, 3, 1, 1, 1]),
        (([1, 2, 4, 6, 7],), [1, 1, 1, 1, 1]),
    ]
    for _, ((cost,), expected) in enumerate(test_cases):
        assert Solution().minCosts(cost) == expected
