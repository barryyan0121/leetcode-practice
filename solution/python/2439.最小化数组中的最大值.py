"""2439. 最小化数组中的最大值"""


class Solution:
    def minimizeArrayValue(self, nums: list[int]) -> int:
        total = answer = 0
        for index, value in enumerate(nums, 1):
            total += value
            answer = max(answer, (total + index - 1) // index)
        return answer


if __name__ == "__main__":
    test_cases = [(([3, 7, 1, 6],), 5)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().minimizeArrayValue(*args) == expected
