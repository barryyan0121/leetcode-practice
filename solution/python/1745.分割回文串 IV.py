class Solution:
    def checkPartitioning(self, s: str) -> bool:
        n = len(s)
        palindrome = [bytearray(n) for _ in range(n)]
        for left in range(n - 1, -1, -1):
            for right in range(left, n):
                if s[left] == s[right] and (
                    right - left < 2 or palindrome[left + 1][right - 1]
                ):
                    palindrome[left][right] = 1
        for first in range(n - 2):
            if not palindrome[0][first]:
                continue
            for second in range(first + 1, n - 1):
                if palindrome[first + 1][second] and palindrome[second + 1][n - 1]:
                    return True
        return False


if __name__ == "__main__":
    solution = Solution()
    assert solution.checkPartitioning("abcbdd") is True
    assert solution.checkPartitioning("bcbddxy") is False
    print("1745 passed")
