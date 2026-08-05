"""2554. 从一个范围内选择最多整数 I"""


class Solution:
    def maxCount(self, banned: list[int], n: int, maxSum: int) -> int:
        banned_set = set(banned)
        answer = 0
        total = 0
        for number in range(1, n + 1):
            if number not in banned_set and total + number <= maxSum:
                total += number
                answer += 1
        return answer


if __name__ == "__main__":
    test_cases = [(([1, 6, 5], 5, 6), 2)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().maxCount(*args) == expected
