"""1909. 删除一个元素使数组严格递增"""


class Solution:
    def canBeIncreasing(self, nums: list[int]) -> bool:
        removed = False
        previous = nums[0]
        for index in range(1, len(nums)):
            if nums[index] <= previous:
                if removed:
                    return False
                removed = True
                if index == 1 or nums[index] > nums[index - 2]:
                    previous = nums[index]
            else:
                previous = nums[index]
        return True


if __name__ == "__main__":
    test_cases = [([1, 2, 10, 5, 7], True), ([2, 3, 1, 2], False)]
    for _, (nums, expected) in enumerate(test_cases):
        assert Solution().canBeIncreasing(nums) == expected
