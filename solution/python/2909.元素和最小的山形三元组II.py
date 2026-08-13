class Solution:
    def minimumSum(self, nums: list[int]) -> int:
        n = len(nums)
        left = [nums[0]]
        for i in range(1, n):
            left.append(min(left[-1], nums[i]))
        right = [0] * n
        right[-1] = nums[-1]
        for i in range(n - 2, -1, -1):
            right[i] = min(right[i + 1], nums[i])
        answer = 10**18
        for i in range(1, n - 1):
            if left[i - 1] < nums[i] and right[i + 1] < nums[i]:
                answer = min(answer, left[i - 1] + nums[i] + right[i + 1])
        return -1 if answer == 10**18 else answer


if __name__ == "__main__":
    assert Solution().minimumSum([8, 6, 1, 5, 3]) == 9
