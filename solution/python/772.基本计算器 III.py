#
# @lc app=leetcode.cn id=772 lang=python3
#
# [772] 基本计算器 III
#


# @lc code=start
class Solution:
    def calculate(self, s):
        index = 0

        def expression():
            nonlocal index
            value = term()
            while True:
                while index < len(s) and s[index] == " ":
                    index += 1
                if index == len(s) or s[index] not in "+-":
                    break
                operator = s[index]
                index += 1
                right = term()
                value = value + right if operator == "+" else value - right
            return value

        def term():
            nonlocal index
            value = factor()
            while True:
                while index < len(s) and s[index] == " ":
                    index += 1
                if index == len(s) or s[index] not in "*/":
                    break
                operator = s[index]
                index += 1
                right = factor()
                value = value * right if operator == "*" else int(value / right)
            return value

        def factor():
            nonlocal index
            while index < len(s) and s[index] == " ":
                index += 1
            if s[index] == "(":
                index += 1
                value = expression()
                index += 1
                return value
            start = index
            while index < len(s) and s[index].isdigit():
                index += 1
            return int(s[start:index])

        return expression()


# @lc code=end


if __name__ == "__main__":
    assert Solution().calculate("1+1") == 2
    assert Solution().calculate("6-4 / 2") == 4
    assert Solution().calculate("2*(5+5*2)/3+(6/2+8)") == 21
