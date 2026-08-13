from typing import List


class Solution:
    def maximumAND(self, nums: List[int], k: int, m: int) -> int:
        def cost(value: int, mask: int) -> int:
            if value & mask == mask:
                return 0
            best = 10**30
            for bit in range(32):
                if value >> bit & 1:
                    continue
                high_mask = ~((1 << (bit + 1)) - 1)
                high = value & high_mask
                if high & (mask & high_mask) != (mask & high_mask):
                    continue
                target = high | (1 << bit) | (mask & ((1 << (bit + 1)) - 1))
                best = min(best, target - value)
            return best

        answer = 0
        for bit in range(31, -1, -1):
            candidate = answer | (1 << bit)
            costs = sorted(cost(value, candidate) for value in nums)
            if sum(costs[:m]) <= k:
                answer = candidate
        return answer


if __name__ == "__main__":
    s = Solution()
    assert s.maximumAND([3, 1, 2], 8, 2) == 6
    assert s.maximumAND([1, 2, 8, 4], 7, 3) == 4
    assert s.maximumAND([1, 1], 3, 2) == 2
