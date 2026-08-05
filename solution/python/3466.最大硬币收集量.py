class Solution:
    def maxCoins(self, lane1: list[int], lane2: list[int]) -> int:
        negative = -(10**30)
        lane1_zero = lane2_one = lane1_two = negative
        answer = negative
        for first, second in zip(lane1, lane2):
            next_lane1_zero = first + max(0, lane1_zero)
            next_lane2_one = second + max(0, lane1_zero, lane2_one)
            next_lane1_two = first + max(lane2_one, lane1_two)
            lane1_zero, lane2_one, lane1_two = (
                next_lane1_zero,
                next_lane2_one,
                next_lane1_two,
            )
            answer = max(answer, lane1_zero, lane2_one, lane1_two)
        return answer


if __name__ == "__main__":
    test_cases = [
        (([1, -2, -10, 3], [-5, 10, 0, 1]), 14),
        (([1, -1, -1, -1], [0, 3, 4, -5]), 8),
        (([-5, -4, -3], [-1, 2, 3]), 5),
        (([-3, -3, -3], [9, -2, 4]), 11),
        (([-10], [-2]), -2),
    ]
    for _, ((lane1, lane2), expected) in enumerate(test_cases):
        assert Solution().maxCoins(lane1, lane2) == expected
