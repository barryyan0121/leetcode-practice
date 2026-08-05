"""2444. 统计定界子数组的数目"""


class Solution:
    def countSubarrays(self, nums: list[int], minK: int, maxK: int) -> int:
        answer = 0
        left = last_min = last_max = -1
        for index, value in enumerate(nums):
            if value < minK or value > maxK:
                left = index
            if value == minK:
                last_min = index
            if value == maxK:
                last_max = index
            answer += max(0, min(last_min, last_max) - left)
        return answer


if __name__ == "__main__":
    test_cases = [(([1, 3, 5, 2, 7, 5], 1, 5), 2)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().countSubarrays(*args) == expected
