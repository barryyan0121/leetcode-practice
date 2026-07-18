class Solution:
    def twoSumLessThanK(self, nums: list[int], k: int) -> int:
        nums.sort()
        left, right = 0, len(nums) - 1
        answer = -1
        while left < right:
            total = nums[left] + nums[right]
            if total < k:
                answer = max(answer, total)
                left += 1
            else:
                right -= 1
        return answer


if __name__ == "__main__":
    test_cases = [
        ([34, 23, 1, 24, 75, 33, 54, 8], 60, 58),
        ([10, 20, 30], 15, -1),
        ([1], 2, -1),
        ([1, 2], 3, -1),
        ([5, 5], 11, 10),
        ([1, 8, 9], 11, 10),
    ]
    for _, (nums, k, expected) in enumerate(test_cases):
        assert Solution().twoSumLessThanK(nums, k) == expected
