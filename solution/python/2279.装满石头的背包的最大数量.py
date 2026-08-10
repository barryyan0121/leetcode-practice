"""2279. 装满石头的背包的最大数量"""


class Solution:
    def maximumBags(
        self, capacity: list[int], rocks: list[int], additionalRocks: int
    ) -> int:
        answer = 0
        for need in sorted(c - r for c, r in zip(capacity, rocks)):
            if need > additionalRocks:
                break
            additionalRocks -= need
            answer += 1
        return answer
