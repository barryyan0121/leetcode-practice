#
# @lc app=leetcode.cn id=824 lang=python3
#
# [824] 山羊拉丁文
#

import os
import sys


# @lc code=start
class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        vowels = set("aeiouAEIOU")
        answer = []
        for index, word in enumerate(sentence.split(), 1):
            if word[0] not in vowels:
                word = word[1:] + word[0]
            answer.append(word + "ma" + "a" * index)
        return " ".join(answer)


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (
            solution.toGoatLatin,
            ("I speak Goat Latin",),
            "Imaa peaksmaaa oatGmaaaa atinLmaaaaa",
        ),
        (
            solution.toGoatLatin,
            ("The quick brown fox jumped over the lazy dog",),
            "heTmaa uickqmaaa rownbmaaaa oxfmaaaaa umpedjmaaaaaa overmaaaaaaa hetmaaaaaaaa azylmaaaaaaaaa ogdmaaaaaaaaaa",
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
