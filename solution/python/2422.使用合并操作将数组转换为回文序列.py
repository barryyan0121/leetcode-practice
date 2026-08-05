"""2422. 使用合并操作将数组转换为回文序列"""


class Solution:
    def minimumOperations(self, nums: list[int]) -> int:
        left, right, answer = 0, len(nums) - 1, 0
        while left < right:
            if nums[left] == nums[right]:
                left += 1
                right -= 1
            elif nums[left] < nums[right]:
                nums[left + 1] += nums[left]
                left += 1
                answer += 1
            else:
                nums[right - 1] += nums[right]
                right -= 1
                answer += 1
        return answer


if __name__ == "__main__":
    test_cases = [(([4, 3, 2, 1, 2, 3, 1],), 2)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().minimumOperations(*args) == expected
