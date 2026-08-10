from typing import List


class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        left = total = answer = 0
        for right, value in enumerate(nums):
            total += value
            while value * (right - left + 1) - total > k:
                total -= nums[left]
                left += 1
            answer = max(answer, right - left + 1)
        return answer


if __name__ == "__main__":
    solution = Solution()
    assert solution.maxFrequency([1, 2, 4], 5) == 3
    assert solution.maxFrequency([1, 4, 8, 13], 5) == 2
    print("1838 passed")
