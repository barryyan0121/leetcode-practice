"""2012. 数组美丽值求和"""


class Solution:
    def sumOfBeauties(self, nums: list[int]) -> int:
        n = len(nums)
        right = [0] * n
        right[-1] = nums[-1]
        for i in range(n - 2, -1, -1):
            right[i] = min(nums[i], right[i + 1])
        left = nums[0]
        answer = 0
        for i in range(1, n - 1):
            if left < nums[i] < right[i + 1]:
                answer += 2
            elif nums[i - 1] < nums[i] < nums[i + 1]:
                answer += 1
            left = max(left, nums[i])
        return answer


if __name__ == "__main__":
    test_cases = [(([1, 2, 3],), 2), (([2, 4, 6, 4],), 1)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().sumOfBeauties(*args) == expected
