"""2110. 股票平滑下降阶段"""


class Solution:
    def getDescentPeriods(self, prices: list[int]) -> int:
        answer = current = 1
        for index in range(1, len(prices)):
            current = current + 1 if prices[index] == prices[index - 1] - 1 else 1
            answer += current
        return answer


if __name__ == "__main__":
    test_cases = [(([3, 2, 1, 4],), 7)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().getDescentPeriods(*args) == expected
