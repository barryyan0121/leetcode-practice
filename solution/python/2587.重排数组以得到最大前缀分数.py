"""2587. 重排数组以得到最大前缀分数"""


class Solution:
    def maxScore(self, nums: list[int]) -> int:
        total = 0
        for index, value in enumerate(sorted(nums, reverse=True)):
            total += value
            if total <= 0:
                return index
        return len(nums)


if __name__ == "__main__":
    test_cases = [(([-2, -1, 0, 1, 3],), 5)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().maxScore(*args) == expected
