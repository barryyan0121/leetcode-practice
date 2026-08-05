"""2025. 分割数组的最多方案数"""

from collections import Counter


class Solution:
    def waysToPartition(self, nums: list[int], k: int) -> int:
        total = sum(nums)
        prefix = 0
        right = Counter()
        for value in nums[:-1]:
            prefix += value
            right[prefix] += 1
        left = Counter()
        answer = right.get(total // 2, 0) if total % 2 == 0 else 0
        prefix = 0
        for i, value in enumerate(nums):
            if i:
                left[prefix] += 1
                right[prefix] -= 1
            new_total = total - value + k
            if new_total % 2 == 0:
                target = new_total // 2
                answer = max(answer, left[target] + right[(2 * total - new_total) // 2])
            prefix += value
        return answer


if __name__ == "__main__":
    test_cases = [(([2, -1, 2], 3), 1), (([0, 0, 0], 1), 2)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().waysToPartition(*args) == expected
