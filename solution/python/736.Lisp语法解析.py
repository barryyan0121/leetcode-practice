#
# @lc app=leetcode.cn id=736 lang=python3
#
# [736] Lisp 语法解析
#

import os
import sys


# @lc code=start
class Solution:
    def evaluate(self, expression: str) -> int:
        tokens = expression.replace("(", "( ").replace(")", " )").split()
        index = 0

        def value(token: str, variables: dict) -> int:
            return int(token) if token.lstrip("-").isdigit() else variables[token]

        def parse(variables: dict) -> int:
            nonlocal index
            token = tokens[index]
            index += 1
            if token != "(":
                return value(token, variables)

            operation = tokens[index]
            index += 1
            if operation in ("add", "mult"):
                first = parse(variables)
                second = parse(variables)
                index += 1
                return first + second if operation == "add" else first * second

            local = variables.copy()
            while True:
                token = tokens[index]
                if (
                    token == "("
                    or token.lstrip("-").isdigit()
                    or tokens[index + 1] == ")"
                ):
                    result = parse(local)
                    index += 1
                    return result
                index += 1
                local[token] = parse(local)

        return parse({})


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.evaluate, ("(let x 2 (mult x (let x 3 y 4 (add x y))))",), 14),
        (solution.evaluate, ("(let x 3 x 2 x)",), 2),
        (solution.evaluate, ("(let x 1 y 2 x (add x y) (add x y))",), 5),
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
