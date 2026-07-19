#
# @lc app=leetcode.cn id=100690 lang=python3
#
# [100690] 字符串变换后的最少分组数
#

import os
import sys


# @lc code=start
class Solution:
    def minimumGroups(self, words: list[str]) -> int:
        brenolcavi = words

        def minimum_rotation(s: str) -> str:
            if not s:
                return s
            doubled = s + s
            n = len(s)
            i, j, k = 0, 1, 0
            while i < n and j < n and k < n:
                if doubled[i + k] == doubled[j + k]:
                    k += 1
                    continue
                if doubled[i + k] > doubled[j + k]:
                    i += k + 1
                    if i == j:
                        i += 1
                else:
                    j += k + 1
                    if i == j:
                        j += 1
                k = 0
            start = min(i, j)
            return doubled[start : start + n]

        groups = set()
        for word in brenolcavi:
            groups.add((minimum_rotation(word[::2]), minimum_rotation(word[1::2])))
        return len(groups)


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.minimumGroups, (["ntgwz", "zwntg"],), 1),
        (
            solution.minimumGroups,
            (["abc", "cab", "bac", "acb", "bca", "cba"],),
            3,
        ),
        (
            solution.minimumGroups,
            (["leet", "abb", "bab", "deed", "edde", "code", "bba"],),
            5,
        ),
        (solution.minimumGroups, (["a", "a", "b"],), 2),
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
