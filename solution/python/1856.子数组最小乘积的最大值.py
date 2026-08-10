from typing import List


class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        prefix = [0]
        for value in nums:
            prefix.append(prefix[-1] + value)
        stack = []
        answer = 0
        for right in range(len(nums) + 1):
            current = nums[right] if right < len(nums) else 0
            while stack and nums[stack[-1]] >= current:
                index = stack.pop()
                left = stack[-1] + 1 if stack else 0
                answer = max(answer, nums[index] * (prefix[right] - prefix[left]))
            stack.append(right)
        return answer % (10**9 + 7)


if __name__ == "__main__":
    solution = Solution()
    assert solution.maxSumMinProduct([1, 2, 3, 2]) == 14
    print("1856 passed")
