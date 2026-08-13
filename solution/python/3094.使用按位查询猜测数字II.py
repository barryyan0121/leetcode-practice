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
