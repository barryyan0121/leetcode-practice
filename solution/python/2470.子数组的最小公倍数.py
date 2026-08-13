"""2470. 子数组的最小公倍数"""

from math import gcd


class Solution:
    def subarrayLCM(self, nums: list[int], k: int) -> int:
        answer = 0
        for start in range(len(nums)):
            current = 1
            for end in range(start, len(nums)):
                current = current * nums[end] // gcd(current, nums[end])
                if current == k:
                    answer += 1
                elif current > k or k % current:
                    break
        return answer


if __name__ == "__main__":
    assert Solution().subarrayLCM([2, 1, 1, 5], 5) == 3
