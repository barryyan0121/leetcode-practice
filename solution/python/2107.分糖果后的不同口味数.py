"""2107. 分糖果后的不同口味数"""


class Solution:
    def shareCandies(self, candies: list[int], k: int) -> int:
        remaining = {}
        for flavor in candies:
            remaining[flavor] = remaining.get(flavor, 0) + 1
        answer = 0
        for index, flavor in enumerate(candies):
            remaining[flavor] -= 1
            if remaining[flavor] == 0:
                del remaining[flavor]
            if index >= k:
                restored = candies[index - k]
                remaining[restored] = remaining.get(restored, 0) + 1
            if index >= k - 1:
                answer = max(answer, len(remaining))
        return answer


if __name__ == "__main__":
    test_cases = [(([1, 2, 2, 3, 4, 3], 3), 3)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().shareCandies(*args) == expected
