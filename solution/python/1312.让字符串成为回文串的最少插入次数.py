class Solution:
    def minInsertions(self, s: str) -> int:
        dp = [0] * len(s)
        for left in range(len(s) - 2, -1, -1):
            previous = 0
            for right in range(left + 1, len(s)):
                current = dp[right]
                if s[left] == s[right]:
                    dp[right] = previous
                else:
                    dp[right] = min(dp[right], dp[right - 1]) + 1
                previous = current
        return dp[-1] if s else 0


if __name__ == "__main__":
    test_cases = [
        (Solution().minInsertions, ("zzazz",), 0),
        (Solution().minInsertions, ("mbadm",), 2),
        (Solution().minInsertions, ("leetcode",), 5),
    ]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1312 题 "让字符串成为回文串的最少插入次数" 所有测试用例通过')
