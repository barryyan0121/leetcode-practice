from math import comb


class Solution:
    def nthSmallest(self, n: int, k: int) -> int:
        length = k
        while n > comb(length - 1, k - 1):
            n -= comb(length - 1, k - 1)
            length += 1
        answer = 1 << (length - 1)
        ones = k - 1
        for bit in range(length - 2, -1, -1):
            if ones == 0:
                break
            count = comb(bit, ones)
            if n > count:
                n -= count
                answer |= 1 << bit
                ones -= 1
        return answer


if __name__ == "__main__":
    assert Solution().nthSmallest(4, 2) == 9
    assert Solution().nthSmallest(3, 1) == 4
