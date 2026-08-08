# @lc app=leetcode.cn id=1307 lang=python3

from typing import List


class Solution:
    def isSolvable(self, words: List[str], result: str) -> bool:
        letters = set("".join(words) + result)
        if len(letters) > 10 or max(map(len, words)) > len(result):
            return False
        leading = {word[0] for word in words + [result] if len(word) > 1}
        reversed_words = [word[::-1] for word in words]
        reversed_result = result[::-1]
        assignment, used = {}, set()

        def dfs(column: int, row: int, total: int) -> bool:
            if column == len(reversed_result):
                return total == 0
            if row < len(reversed_words):
                if column >= len(reversed_words[row]):
                    return dfs(column, row + 1, total)
                letter = reversed_words[row][column]
                if letter in assignment:
                    return dfs(column, row + 1, total + assignment[letter])
                for digit in range(10):
                    if digit in used or (digit == 0 and letter in leading):
                        continue
                    assignment[letter] = digit
                    used.add(digit)
                    if dfs(column, row + 1, total + digit):
                        return True
                    used.remove(digit)
                    del assignment[letter]
                return False
            letter = reversed_result[column]
            digit = total % 10
            carry = total // 10
            if letter in assignment:
                return assignment[letter] == digit and dfs(column + 1, 0, carry)
            if digit in used or (digit == 0 and letter in leading):
                return False
            assignment[letter] = digit
            used.add(digit)
            if dfs(column + 1, 0, carry):
                return True
            used.remove(digit)
            del assignment[letter]
            return False

        return dfs(0, 0, 0)


if __name__ == "__main__":
    test_cases = [
        (Solution().isSolvable, (["SEND", "MORE"], "MONEY"), True),
        (Solution().isSolvable, (["SIX", "SEVEN", "SEVEN"], "TWENTY"), True),
        (Solution().isSolvable, (["LEET", "CODE"], "POINT"), False),
        (Solution().isSolvable, (["WE", "ARE"], "IT"), False),
    ]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1307 题 "口算难题" 所有测试用例通过')
