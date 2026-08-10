"""1896. 改变表达式的最终值的最小代价"""


class Solution:
    def minOperationsToFlip(self, expression: str) -> int:
        inf = 10**9
        digit = int(expression[0])
        costs = [inf] * 4
        costs[digit] = 0
        costs[1 - digit] = 1
        for index in range(1, len(expression), 2):
            operator = expression[index]
            value = int(expression[index + 1])
            next_costs = [inf] * 4
            for state, (sum_value, product_value) in enumerate(
                ((a, b) for a in range(2) for b in range(2))
            ):
                for new_value, digit_cost in ((value, 0), (1 - value, 1)):
                    for new_operator, operator_cost in (
                        (operator, 0),
                        ("+" if operator == "*" else "*", 1),
                    ):
                        if new_operator == "+":
                            new_state = (sum_value | product_value) * 2 + new_value
                        else:
                            new_state = sum_value * 2 + (product_value & new_value)
                        next_costs[new_state] = min(
                            next_costs[new_state],
                            costs[state] + digit_cost + operator_cost,
                        )
            costs = next_costs
        result = int(expression[0])
        for index in range(1, len(expression), 2):
            value = int(expression[index + 1])
            result = (result | value) if expression[index] == "+" else (result & value)
        return min(
            cost
            for state, cost in enumerate(costs)
            if ((state // 2) | (state % 2)) != result
        )


if __name__ == "__main__":
    assert Solution().minOperationsToFlip("1+1+1") == 3
