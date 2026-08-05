class Solution:
    def numberOfGoodSubarraySplits(self, nums: list[int]) -> int:
        mod = 10**9 + 7
        ans = 1
        prev = -1
        found = False
        for i, value in enumerate(nums):
            if value:
                if found:
                    ans = ans * (i - prev) % mod
                found = True
                prev = i
        return ans if found else 0


if __name__ == "__main__":
    assert Solution().numberOfGoodSubarraySplits([0, 1, 0, 0, 1]) == 3
