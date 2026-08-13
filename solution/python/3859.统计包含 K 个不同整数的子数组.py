"""3859. 统计包含 K 个不同整数的子数组"""

from collections import Counter, defaultdict


class Solution:
    def countSubarrays(self, nums: list[int], k: int, m: int) -> int:
        n = len(nums)
        positions: dict[int, list[int]] = defaultdict(list)
        present = Counter()
        enough = Counter()
        answer = 0
        left = 0

        for right, value in enumerate(nums):
            positions[value].append(right)
            present[value] += 1
            if present[value] == m:
                enough[value] = positions[value][-m]

            while len(present) > k:
                removed = nums[left]
                present[removed] -= 1
                if present[removed] == 0:
                    del present[removed]
                    enough.pop(removed, None)
                elif present[removed] == m - 1:
                    enough.pop(removed, None)
                elif present[removed] >= m:
                    enough[removed] = positions[removed][-(m)]
                left += 1

            if len(present) == k and len(enough) == k:
                limit = min(enough.values())
                answer += max(0, limit - left + 1)

        return answer


if __name__ == "__main__":
    test_cases = [(([1, 2, 1, 2, 2], 2, 2), 2), (([3, 1, 2, 4], 2, 1), 3)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().countSubarrays(*args) == expected
