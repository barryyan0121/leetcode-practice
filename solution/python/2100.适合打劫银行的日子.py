"""2100. 适合打劫银行的日子"""


class Solution:
    def goodDaysToRobBank(self, security: list[int], time: int) -> list[int]:
        n = len(security)
        non_increasing = [0] * n
        non_decreasing = [0] * n
        for i in range(1, n):
            if security[i] <= security[i - 1]:
                non_increasing[i] = non_increasing[i - 1] + 1
            if security[i] >= security[i - 1]:
                non_decreasing[i] = non_decreasing[i - 1] + 1
        return [
            i
            for i in range(n)
            if non_increasing[i] >= time
            and i + time < n
            and non_decreasing[i + time] - non_decreasing[i] == time
        ]


if __name__ == "__main__":
    test_cases = [(([5, 3, 3, 3, 5, 6, 2], 2), [2, 3])]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().goodDaysToRobBank(*args) == expected
