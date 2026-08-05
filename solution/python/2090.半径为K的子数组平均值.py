"""2090. 半径为 K 的子数组平均值"""


class Solution:
    def getAverages(self, nums: list[int], k: int) -> list[int]:
        answer = [-1] * len(nums)
        width = 2 * k + 1
        if width > len(nums):
            return answer
        window = sum(nums[:width])
        answer[k] = window // width
        for right in range(width, len(nums)):
            window += nums[right] - nums[right - width]
            answer[right - k] = window // width
        return answer


if __name__ == "__main__":
    test_cases = [(([7, 4, 3, 9, 1, 8, 5, 2, 6], 3), [-1, -1, -1, 5, 4, 4, -1, -1, -1])]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().getAverages(*args) == expected
