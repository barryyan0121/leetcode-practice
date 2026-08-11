"""2845. 统计趣味子数组的数目"""

from collections import defaultdict


class Solution:
    def countInterestingSubarrays(self, nums: list[int], modulo: int, k: int) -> int:
        counts = defaultdict(int)
        counts[0] = 1
        prefix = answer = 0
        for number in nums:
            prefix += number % modulo == k
            answer += counts[(prefix - k) % modulo]
            counts[prefix % modulo] += 1
        return answer


if __name__ == "__main__":
    assert Solution().countInterestingSubarrays([3, 1, 9, 6], 3, 0) == 2
