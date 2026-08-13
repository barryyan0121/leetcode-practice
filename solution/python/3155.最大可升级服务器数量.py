"""3155. 最大可升级服务器数量"""

from typing import List


class Solution:
    def maxUpgrades(
        self, count: List[int], upgrade: List[int], sell: List[int], money: List[int]
    ) -> List[int]:
        ans = []
        for cnt, cost, income, cash in zip(count, upgrade, sell, money):
            ans.append(min(cnt, (cnt * income + cash) // (cost + income)))
        return ans


if __name__ == "__main__":
    f = Solution().maxUpgrades
    assert f([1], [2], [1], [1]) == [0]
    assert f([2, 3], [3, 4], [1, 2], [1, 5]) == [0, 1]
