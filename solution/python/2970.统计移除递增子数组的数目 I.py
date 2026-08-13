class Solution:
    def incremovableSubarrayCount(self, nums: list[int]) -> int:
        answer = 0
        for left in range(len(nums)):
            for right in range(left, len(nums)):
                remain = nums[:left] + nums[right + 1 :]
                if all(a < b for a, b in zip(remain, remain[1:])):
                    answer += 1
        return answer


if __name__ == "__main__":
    solution = Solution()
    assert solution.incremovableSubarrayCount([1, 2, 3, 4]) == 10
    assert solution.incremovableSubarrayCount([6, 5, 7, 8]) == 7
    assert solution.incremovableSubarrayCount([8, 7, 6, 6]) == 3
