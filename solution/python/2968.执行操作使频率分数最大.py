class Solution:
    def maxFrequencyScore(self, nums: list[int], k: int) -> int:
        nums.sort()
        prefix = [0]
        for value in nums:
            prefix.append(prefix[-1] + value)
        left = answer = 0
        for right in range(len(nums)):
            while left <= right:
                middle = (left + right) // 2
                target = nums[middle]
                cost = target * (middle - left) - (prefix[middle] - prefix[left])
                cost += (
                    prefix[right + 1] - prefix[middle + 1] - target * (right - middle)
                )
                if cost <= k:
                    break
                left += 1
            answer = max(answer, right - left + 1)
        return answer


if __name__ == "__main__":
    solution = Solution()
    assert solution.maxFrequencyScore([1, 2, 6, 4], 3) == 3
    assert solution.maxFrequencyScore([1, 4, 4, 2, 4], 0) == 3
