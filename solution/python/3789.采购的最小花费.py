class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        shared = min(need1, need2)
        answer = shared * min(costBoth, cost1 + cost2)
        need1 -= shared
        need2 -= shared
        return answer + need1 * min(cost1, costBoth) + need2 * min(cost2, costBoth)


if __name__ == "__main__":
    s = Solution()
    assert s.minimumCost(3, 2, 1, 3, 2) == 3
    assert s.minimumCost(5, 4, 15, 2, 3) == 22
    assert s.minimumCost(5, 4, 15, 0, 0) == 0
