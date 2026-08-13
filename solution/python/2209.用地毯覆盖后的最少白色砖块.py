"""2209. 用地毯覆盖后的最少白色砖块"""


class Solution:
    def minimumWhiteTiles(self, floor: str, numCarpets: int, carpetLen: int) -> int:
        n = len(floor)
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            dp[i] = dp[i - 1] + (floor[i - 1] == "1")
        for _ in range(numCarpets):
            nxt = dp[:]
            for i in range(1, n + 1):
                nxt[i] = min(
                    nxt[i - 1] + (floor[i - 1] == "1"), dp[max(0, i - carpetLen)]
                )
            dp = nxt
        return dp[n]

if __name__ == "__main__":
    assert Solution().minimumWhiteTiles("10110101", 2, 2) == 2
