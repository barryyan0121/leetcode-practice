"""2263. 数组变为有序的最小操作次数"""


class Solution:
    def convertArray(self, nums: list[int]) -> int:
        values = sorted(set(nums))

        def cost(reverse: bool) -> int:
            dp = [0] * len(values)
            for value in nums:
                previous = dp[:]
                best = 10**18
                indices = (
                    range(len(values) - 1, -1, -1) if reverse else range(len(values))
                )
                for i in indices:
                    best = min(best, previous[i])
                    dp[i] = best + abs(value - values[i])
            return min(dp)

        return min(cost(False), cost(True))

if __name__ == "__main__":
    assert Solution().convertArray([3,2,4,5,0]) == 4
