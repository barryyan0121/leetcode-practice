"""2223. 构造字符串的总得分和"""


class Solution:
    def sumScores(self, s: str) -> int:
        n = len(s)
        z = [0] * n
        left = right = answer = 0
        for i in range(1, n):
            if i <= right:
                z[i] = min(right - i + 1, z[i - left])
            while i + z[i] < n and s[z[i]] == s[i + z[i]]:
                z[i] += 1
            if i + z[i] - 1 > right:
                left, right = i, i + z[i] - 1
            answer += z[i]
        return answer + n

if __name__ == "__main__":
    assert Solution().sumScores("babab") == 9
