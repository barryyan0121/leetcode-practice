# @lc app=leetcode.cn id=1648 lang=python3


class Solution:
    def maxProfit(self, inventory: list[int], orders: int) -> int:
        mod = 10**9 + 7
        inventory.sort(reverse=True)
        inventory.append(0)
        answer = 0
        for index in range(len(inventory) - 1):
            width = index + 1
            levels = inventory[index] - inventory[index + 1]
            total = width * levels
            if orders >= total:
                answer = (
                    answer
                    + width
                    * (inventory[index] + inventory[index + 1] + 1)
                    * levels
                    // 2
                ) % mod
                orders -= total
            else:
                full, remainder = divmod(orders, width)
                answer = (
                    answer
                    + width
                    * (inventory[index] + inventory[index] - full + 1)
                    * full
                    // 2
                    + remainder * (inventory[index] - full)
                ) % mod
                break
        return answer


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.maxProfit, ([2, 5], 4), 14),
        (solution.maxProfit, ([3, 5], 6), 19),
    ]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1648 题 "销售价值减少的颜色球" 所有测试用例通过')
