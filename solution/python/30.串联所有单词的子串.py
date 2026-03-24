#
# @lc app=leetcode.cn id=30 lang=python3
#
# [30] 串联所有单词的子串
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []

        word_len = len(words[0])
        total_len = word_len * len(words)
        if len(s) < total_len:
            return []

        need = {}
        for word in words:
            need[word] = need.get(word, 0) + 1

        ans = []
        for offset in range(word_len):
            left = offset
            count = 0
            window = {}

            for right in range(offset, len(s) - word_len + 1, word_len):
                word = s[right : right + word_len]
                if word in need:
                    window[word] = window.get(word, 0) + 1
                    count += 1

                    while window[word] > need[word]:
                        left_word = s[left : left + word_len]
                        window[left_word] -= 1
                        count -= 1
                        left += word_len

                    if count == len(words):
                        ans.append(left)
                        left_word = s[left : left + word_len]
                        window[left_word] -= 1
                        count -= 1
                        left += word_len
                else:
                    window.clear()
                    count = 0
                    left = right + word_len

        return sorted(ans)


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    # 测试用例 (func, args, result)
    test_cases = [
        (
            solution.findSubstring,
            ("barfoothefoobarman", ["foo", "bar"]),
            [0, 9],
        ),
        (
            solution.findSubstring,
            ("wordgoodgoodgoodbestword", ["word", "good", "best", "word"]),
            [],
        ),
        (
            solution.findSubstring,
            ("barfoofoobarthefoobarman", ["bar", "foo", "the"]),
            [6, 9, 12],
        ),
        (solution.findSubstring, ("aaaaaa", ["aa", "aa"]), [0, 1, 2]),
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
# "barfoothefoobarman"\n["foo","bar"]\n
# @lcpr case=end

#
