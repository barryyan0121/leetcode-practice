#
# @lc app=leetcode.cn id=770 lang=python3
#
# [770] 基本计算器 IV
#

import os
import re
import sys
from collections import defaultdict
from typing import Dict, List, Tuple


# @lc code=start
class Solution:
    def basicCalculatorIV(
        self, expression: str, evalvars: List[str], evalints: List[int]
    ) -> List[str]:
        values = dict(zip(evalvars, evalints))
        tokens = re.findall(r"[a-z]+|\d+|[()+*-]", expression)
        index = 0
        Polynomial = Dict[Tuple[str, ...], int]

        def add(left: Polynomial, right: Polynomial, sign: int = 1) -> Polynomial:
            result = defaultdict(int, left)
            for monomial, coefficient in right.items():
                result[monomial] += sign * coefficient
            return {
                monomial: coefficient
                for monomial, coefficient in result.items()
                if coefficient
            }

        def multiply(left: Polynomial, right: Polynomial) -> Polynomial:
            result = defaultdict(int)
            for left_monomial, left_coefficient in left.items():
                for right_monomial, right_coefficient in right.items():
                    result[tuple(sorted(left_monomial + right_monomial))] += (
                        left_coefficient * right_coefficient
                    )
            return {
                monomial: coefficient
                for monomial, coefficient in result.items()
                if coefficient
            }

        def factor() -> Polynomial:
            nonlocal index
            if tokens[index] in "+-":
                sign = -1 if tokens[index] == "-" else 1
                index += 1
                return {
                    monomial: sign * coefficient
                    for monomial, coefficient in factor().items()
                }
            token = tokens[index]
            index += 1
            if token == "(":
                result = expression_value()
                index += 1
                return result
            if token.isdigit():
                return {(): int(token)}
            return {(): values[token]} if token in values else {(token,): 1}

        def term() -> Polynomial:
            nonlocal index
            result = factor()
            while index < len(tokens) and tokens[index] == "*":
                index += 1
                result = multiply(result, factor())
            return result

        def expression_value() -> Polynomial:
            nonlocal index
            result = term()
            while index < len(tokens) and tokens[index] in "+-":
                operator = tokens[index]
                index += 1
                result = add(result, term(), 1 if operator == "+" else -1)
            return result

        polynomial = {
            monomial: coefficient
            for monomial, coefficient in expression_value().items()
            if coefficient
        }
        ordered = sorted(polynomial, key=lambda monomial: (-len(monomial), monomial))
        return [
            str(polynomial[monomial]) + ("*" + "*".join(monomial) if monomial else "")
            for monomial in ordered
        ]


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.basicCalculatorIV, ("e + 8 - a + 5", ["e"], [1]), ["-1*a", "14"]),
        (
            solution.basicCalculatorIV,
            ("(e + 8) * (e - 8)", [], []),
            ["1*e*e", "-64"],
        ),
        (
            solution.basicCalculatorIV,
            ("7 - 7", [], []),
            [],
        ),
        (solution.basicCalculatorIV, ("0", [], []), []),
    ]
    all_passed = True
    for idx, (func, args, expected) in enumerate(test_cases):
        result = func(*args)
        try:
            assert result == expected
            print(f"测试用例 {idx + 1} 通过: n = {args}, result = {result}")
        except AssertionError:
            all_passed = False
            print(
                f"测试用例 {idx + 1} 失败: n = {args}, 期望 = {expected}, 实际 = {result}"
            )
    file_path = os.path.basename(__file__).split(".")
    if all_passed:
        print(f'第 {file_path[0]} 题 "{file_path[1]}" 所有测试用例通过')
        sys.exit(0)
    sys.exit(1)
