#
# @lc app=leetcode.cn id=418 lang=python3
# @lcpr version=30203
#
# [418] 屏幕可显示句子的数量
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def wordsTyping(self, sentence: List[str], rows: int, cols: int) -> int:
        text = " ".join(sentence) + " "
        n = len(text)
        pos = 0
        for _ in range(rows):
            pos += cols
            if text[pos % n] == " ":
                pos += 1
            else:
                while pos > 0 and text[(pos - 1) % n] != " ":
                    pos -= 1
        return pos // n


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    # 测试用例 (func, args, result)
    test_cases = [
        (solution.wordsTyping, (["hello", "world"], 2, 8), 1),
        (solution.wordsTyping, (["a", "bcd", "e"], 3, 6), 2),
        (solution.wordsTyping, (["a"], 1, 1), 1),
    ]

    all_passed = True
    for idx, (func, args, expected) in enumerate(test_cases):
        try:
            result = func(*args)
            assert result == expected
            print(f"测试用例 {idx + 1} 通过: n = {args}, result = {result}")
        except AssertionError:
            all_passed = False
            print(
                f"测试用例 {idx + 1} 失败: n = {args}, 期望 = {expected}, 实际 = {result}"
            )

    file_path = os.path.basename(__file__).split(".")
    file_number = file_path[0]
    file_name = file_path[1]
    if all_passed:
        print(f'第 {file_number} 题 "{file_name}" 所有测试用例通过')
        sys.exit(0)
    else:
        print(f'第 {file_number} 题 "{file_name}" 部分测试用例失败')
        sys.exit(1)


#
# @lcpr case=start
# ["hello","world"]\n2\n8\n
# @lcpr case=end

#
