from math import gcd


class Solution:
    def countBeautifulPairs(self, nums: list[int]) -> int:
        ans = 0
        for i, a in enumerate(nums):
            for b in nums[i + 1 :]:
                if gcd(int(str(a)[0]), b % 10) == 1:
                    ans += 1
        return ans


if __name__ == "__main__":
    assert Solution().countBeautifulPairs([2, 5, 1, 4]) == 5
