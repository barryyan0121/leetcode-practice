class Solution:
    def minAllOneMultiple(self, k: int) -> int:
        if k % 2 == 0 or k % 5 == 0:
            return -1
        remainder = 0
        seen = set()
        length = 0
        while remainder not in seen:
            seen.add(remainder)
            remainder = (remainder * 10 + 1) % k
            length += 1
            if remainder == 0:
                return length
        return -1


if __name__ == "__main__":
    s = Solution()
    assert s.minAllOneMultiple(3) == 3
    assert s.minAllOneMultiple(7) == 6
    assert s.minAllOneMultiple(2) == -1
