"""2902. 有界子多重集合的数目"""

from collections import Counter


class Solution:
    def countSubMultisets(self, nums: list[int], l: int, r: int) -> int:
        modulo = 10**9 + 7
        counts = Counter(nums)
        dp = [0] * (r + 1)
        dp[0] = 1
        for value, count in counts.items():
            if value == 0:
                factor = count + 1
                dp = [entry * factor % modulo for entry in dp]
                continue
            updated = [0] * (r + 1)
            for remainder in range(min(value, r + 1)):
                window = 0
                for total in range(remainder, r + 1, value):
                    window = (window + dp[total]) % modulo
                    expired = total - (count + 1) * value
                    if expired >= 0:
                        window = (window - dp[expired]) % modulo
                    updated[total] = window
            dp = updated
        return sum(dp[l : r + 1]) % modulo


if __name__ == "__main__":
    assert Solution().countSubMultisets([1, 2, 2, 3], 2, 4) == 5
