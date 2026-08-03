class Solution:
    def resultArray(self, nums: list[int]) -> list[int]:
        first = [nums[0]]
        second = [nums[1]]
        for number in nums[2:]:
            if first[-1] > second[-1]:
                first.append(number)
            else:
                second.append(number)
        return first + second


if __name__ == "__main__":
    test_cases = [([2, 1, 3], [2, 3, 1]), ([5, 4, 3, 8], [5, 3, 4, 8])]
    for _, (nums, expected) in enumerate(test_cases):
        assert Solution().resultArray(nums) == expected
