class Solution:
    def findNumber(self) -> int:
        base = commonBits(0)
        ans = 0
        for i in range(30):
            probe = 1 << i
            current = commonBits(probe)
            if current > base:
                ans |= probe
            commonBits(probe)
        return ans


if __name__ == "__main__":
    target = 37

    def commonBits(x):
        return 1 if x & target else 0

    s = Solution()
    assert s.findNumber() == target
    print("3094 ok")
