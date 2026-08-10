"""2875. 无限数组的最短子数组"""


class Solution:
    def minSizeSubarray(self, nums: list[int], target: int) -> int:
        total = sum(nums)
        cycles, remainder = divmod(target, total)
        if remainder == 0:
            return cycles * len(nums)
        answer = len(nums) + 1
        left = current = 0
        doubled = nums * 2
        for right, value in enumerate(doubled):
            current += value
            while current > remainder:
                current -= doubled[left]
                left += 1
            if current == remainder:
                answer = min(answer, right - left + 1)
        return cycles * len(nums) + answer


if __name__ == "__main__":
    assert Solution().minSizeSubarray([1, 2, 3], 5) == 2
