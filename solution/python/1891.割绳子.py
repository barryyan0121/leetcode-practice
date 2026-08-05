"""1891. 割绳子"""


class Solution:
    def maxLength(self, ribbons: list[int], k: int) -> int:
        low, high = 1, max(ribbons)
        answer = 0
        while low <= high:
            middle = (low + high) // 2
            pieces = sum(ribbon // middle for ribbon in ribbons)
            if pieces >= k:
                answer = middle
                low = middle + 1
            else:
                high = middle - 1
        return answer


if __name__ == "__main__":
    test_cases = [(([9, 7, 5], 3), 5), (([7, 5, 9], 4), 4)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().maxLength(*args) == expected
