"""1995. 统计特殊四元组"""


class Solution:
    def countQuadruplets(self, nums: list[int]) -> int:
        answer = 0
        counts = {}
        for c in range(2, len(nums) - 1):
            for a in range(c - 1):
                total = nums[a] + nums[c - 1]
                counts[total] = counts.get(total, 0) + 1
            for d in range(c + 1, len(nums)):
                answer += counts.get(nums[d] - nums[c], 0)
        return answer


if __name__ == "__main__":
    test_cases = [(([1, 2, 3, 6],), 1)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().countQuadruplets(*args) == expected
