class Solution:
    def almostPalindromic(self, s: str) -> int:
        n = len(s)
        pal = [bytearray(n) for _ in range(n)]
        almost = [bytearray(n) for _ in range(n)]
        answer = 1
        for length in range(1, n + 1):
            for left in range(n - length + 1):
                right = left + length - 1
                if s[left] == s[right] and (length <= 2 or pal[left + 1][right - 1]):
                    pal[left][right] = 1
                if s[left] == s[right]:
                    almost[left][right] = length <= 2 or almost[left + 1][right - 1]
                elif length == 2 or pal[left + 1][right] or pal[left][right - 1]:
                    almost[left][right] = 1
                if almost[left][right]:
                    answer = length
        return answer


if __name__ == "__main__":
    assert Solution().almostPalindromic("abca") == 4
    assert Solution().almostPalindromic("abba") == 4
    assert Solution().almostPalindromic("zzabba") == 5
    assert Solution().almostPalindromic("aba") == 3
