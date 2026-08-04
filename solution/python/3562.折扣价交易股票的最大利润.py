"""3562. 折扣价交易股票的最大利润"""


class Solution:
    def maxProfit(
        self,
        n: int,
        present: list[int],
        future: list[int],
        hierarchy: list[list[int]],
        budget: int,
    ) -> int:
        blenorvask = (present, future, hierarchy, budget)
        children = [[] for _ in range(n)]
        for manager, employee in hierarchy:
            children[manager - 1].append(employee - 1)

        order = [0]
        for node in order:
            order.extend(children[node])

        impossible = -(10**9)
        dp0 = [None] * n
        dp1 = [None] * n
        for node in reversed(order):
            not_buy = [0] + [impossible] * budget
            buy_children = [0] + [impossible] * budget
            for child in children[node]:
                child_not = dp0[child]
                child_buy = dp1[child]
                next_not = [impossible] * (budget + 1)
                next_buy = [impossible] * (budget + 1)
                for used in range(budget + 1):
                    if not_buy[used] == impossible and buy_children[used] == impossible:
                        continue
                    for extra in range(budget - used + 1):
                        if (
                            not_buy[used] != impossible
                            and child_not[extra] != impossible
                        ):
                            next_not[used + extra] = max(
                                next_not[used + extra], not_buy[used] + child_not[extra]
                            )
                        if (
                            buy_children[used] != impossible
                            and child_buy[extra] != impossible
                        ):
                            next_buy[used + extra] = max(
                                next_buy[used + extra],
                                buy_children[used] + child_buy[extra],
                            )
                not_buy, buy_children = next_not, next_buy

            def make_state(cost):
                result = not_buy[:]
                gain = future[node] - cost
                for used in range(cost, budget + 1):
                    if buy_children[used - cost] != impossible:
                        result[used] = max(
                            result[used], buy_children[used - cost] + gain
                        )
                return result

            dp0[node] = make_state(present[node])
            dp1[node] = make_state(present[node] // 2)

        return max(dp0[0])


if __name__ == "__main__":
    test_cases = [
        ((2, [1, 2], [4, 3], [[1, 2]], 3), 5),
        ((2, [3, 4], [5, 8], [[1, 2]], 4), 4),
        ((3, [4, 6, 8], [7, 9, 11], [[1, 2], [1, 3]], 10), 10),
        ((3, [5, 2, 3], [8, 5, 6], [[1, 2], [2, 3]], 7), 12),
    ]
    for _, ((n, present, future, hierarchy, budget), expected) in enumerate(test_cases):
        assert Solution().maxProfit(n, present, future, hierarchy, budget) == expected
