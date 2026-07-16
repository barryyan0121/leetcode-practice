#
# @lc app=leetcode.cn id=917 lang=python3
#
# [917] 仅仅反转字母
#

import os
import sys


# @lc code=start
class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        characters = list(s)
        left, right = 0, len(characters) - 1
        while left < right:
            if not characters[left].isalpha():
                left += 1
            elif not characters[right].isalpha():
                right -= 1
            else:
                characters[left], characters[right] = (
                    characters[right],
                    characters[left],
                )
                left += 1
                right -= 1
        return "".join(characters)


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.reverseOnlyLetters, ("ab-cd",), "dc-ba"),
        (solution.reverseOnlyLetters, ("a-bC-dEf-ghIj",), "j-Ih-gfE-dCba"),
        (
            solution.reverseOnlyLetters,
            ("Test1ng-Leet=code-Q!",),
            "Qedo1ct-eeLg=ntse-T!",
        ),
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
