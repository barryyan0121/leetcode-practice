class Solution:
    def checkDivisibility(self, n: int) -> bool:
        s = 0
        p = 1
        for ch in str(n):
            d = ord(ch) - 48
            s += d
            p *= d
        return n % (s + p) == 0


if __name__ == "__main__":
    s = Solution()
    assert s.checkDivisibility(99) is True
    assert s.checkDivisibility(23) is False
    print("3622 ok")
