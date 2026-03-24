#
# @lc app=leetcode.cn id=68 lang=python3
#
# [68] 文本左右对齐
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        ans = []
        i = 0

        while i < len(words):
            line_len = len(words[i])
            j = i + 1
            while j < len(words) and line_len + 1 + len(words[j]) <= maxWidth:
                line_len += 1 + len(words[j])
                j += 1

            line_words = words[i:j]
            spaces = maxWidth - sum(len(word) for word in line_words)

            if j == len(words) or len(line_words) == 1:
                line = " ".join(line_words).ljust(maxWidth)
            else:
                gaps = len(line_words) - 1
                base, extra = divmod(spaces, gaps)
                pieces = []
                for idx, word in enumerate(line_words[:-1]):
                    pieces.append(word)
                    pieces.append(" " * (base + (1 if idx < extra else 0)))
                pieces.append(line_words[-1])
                line = "".join(pieces)

            ans.append(line)
            i = j

        return ans


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    # 测试用例 (func, args, result)
    test_cases = [
        (
            solution.fullJustify,
            (["This", "is", "an", "example", "of", "text", "justification."], 16),
            ["This    is    an", "example  of text", "justification.  "],
        ),
        (
            solution.fullJustify,
            (["What", "must", "be", "acknowledgment", "shall", "be"], 16),
            ["What   must   be", "acknowledgment  ", "shall be        "],
        ),
        (
            solution.fullJustify,
            (["Science", "is", "what", "we", "understand", "well"], 20),
            ["Science  is  what we", "understand well     "],
        ),
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
# ["This","is","an","example","of","text","justification."]\n16\n
# @lcpr case=end
