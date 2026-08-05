"""2640. 一个数组所有前缀的分数"""


class Solution:
    def findPrefixScore(self, nums: list[int]) -> list[int]:
        answer = []
        total = maximum = 0
        for value in nums:
            maximum = max(maximum, value)
            total += value + maximum
            answer.append(total)
        return answer


if __name__ == "__main__":
    test_cases = [(([2, 3, 7, 5, 10],), [4, 10, 24, 36, 56])]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().findPrefixScore(*args) == expected
