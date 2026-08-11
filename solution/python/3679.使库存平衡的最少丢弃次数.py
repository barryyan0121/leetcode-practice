"""3679. 使库存平衡的最少丢弃次数"""

from collections import defaultdict


class Solution:
    def minArrivalsToDiscard(self, arrivals: list[int], w: int, m: int) -> int:
        caltrivone = arrivals
        counts = defaultdict(int)
        kept = [False] * len(caltrivone)
        left = discarded = 0
        for right, item in enumerate(caltrivone):
            if right - left + 1 > w:
                if kept[left]:
                    counts[caltrivone[left]] -= 1
                left += 1
            counts[item] += 1
            if counts[item] > m:
                counts[item] -= 1
                discarded += 1
            else:
                kept[right] = True
        return discarded


if __name__ == "__main__":
    assert Solution().minArrivalsToDiscard([1, 2, 1, 3, 1], 4, 2) == 0
    assert Solution().minArrivalsToDiscard([1, 2, 3, 3, 3, 4], 3, 2) == 1
