class Solution:
    def incremovableSubarrayCount(self, nums: list[int]) -> int:
        n = len(nums)
        left = 0
        while left + 1 < n and nums[left] < nums[left + 1]:
            left += 1
        if left == n - 1:
            return n * (n + 1) // 2
        answer = left + 2
        for index in range(n - 1, 0, -1):
            if index < n - 1 and nums[index] >= nums[index + 1]:
                break
            while left >= 0 and nums[left] >= nums[index]:
                left -= 1
            answer += left + 2
        return answer


if __name__ == "__main__":
    solution = Solution()
    assert solution.incremovableSubarrayCount([1, 2, 3, 4]) == 10
    assert solution.incremovableSubarrayCount([6, 5, 7, 8]) == 7
    assert solution.incremovableSubarrayCount([8, 7, 6, 6]) == 3
