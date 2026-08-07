#
# @lc app=leetcode.cn id=656 lang=python3
#
# [656] 成本最小路径
#


# @lc code=start
class Solution:
    def cheapestJump(self, coins, maxJump):
        n = len(coins)
        costs = [float("inf")] * n
        paths = [None] * n
        costs[0], paths[0] = coins[0], [1]
        for i in range(1, n):
            if coins[i] == -1:
                continue
            for j in range(max(0, i - maxJump), i):
                if paths[j] is None:
                    continue
                candidate_cost = costs[j] + coins[i]
                candidate_path = paths[j] + [i + 1]
                if candidate_cost < costs[i] or (
                    candidate_cost == costs[i] and candidate_path < paths[i]
                ):
                    costs[i], paths[i] = candidate_cost, candidate_path
        return paths[-1] or []


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    assert solution.cheapestJump([1, 2, 4, -1, 2], 2) == [1, 3, 5]
    assert solution.cheapestJump([1, 2, 4, -1, 2], 1) == []
