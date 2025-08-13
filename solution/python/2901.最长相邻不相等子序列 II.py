#
# @lc app=leetcode.cn id=2901 lang=python3
# @lcpr version=30202
#
# [2901] 最长相邻不相等子序列 II
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
class Solution:
    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:

        def hanming(s1, s2):
            dis = 0
            for i in range(len(s1)):
                if s1[i] != s2[i]:
                    dis += 1
                    if dis > 1:
                        return False
            return True if dis == 1 else False

        ws = [[] for i in range(10)]
        gs = [[] for i in range(10)]
        for i in range(len(words)):
            l = len(words[i]) - 1
            ws[l].append(words[i])
            gs[l].append(groups[i])
        max_len = 0
        ret = None
        for i in range(10):
            w, g = ws[i], gs[i]
            n = len(w)
            if n == 0:
                continue
            p, dp = [-1] * n, [1] * n
            m, m_idx = 1, 0
            for j in range(1, n):
                for k in range(j):
                    if g[j] != g[k] and hanming(w[j], w[k]) and dp[k] >= dp[j]:
                        dp[j] = dp[k] + 1
                        p[j] = k
                if dp[j] > m:
                    m = dp[j]
                    m_idx = j
            if m > max_len:
                this = []
                while m_idx >= 0:
                    this.append(w[m_idx])
                    m_idx = p[m_idx]
                this.reverse()
                ret = this
                max_len = m

        return ret
        # @lc code=end


if __name__ == '__main__':
    solution = Solution()
    # 测试用例 (func, args, result)
    test_cases = [
        (solution.getWordsInLongestSubsequence, [["bab", "dab", "cab"], [1, 2, 2]], ["bab", "dab"]),
        (solution.getWordsInLongestSubsequence, [["a", "b", "c", "d"], [1, 2, 3, 4]], ["a", "b", "c", "d"]),
    ]

    all_passed = True
    for idx, (func, args, expected) in enumerate(test_cases):
        try:
            result = func(*args)
            assert result == expected
            print(f"测试用例 {idx + 1} 通过: n = {args}, result = {result}")
        except AssertionError:
            all_passed = False
            print(f"测试用例 {idx + 1} 失败: n = {args}, 期望 = {expected}, 实际 = {result}")

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
# ["bab","dab","cab"]\n[1,2,2]\n
# @lcpr case=end

# @lcpr case=start
# ["a","b","c","d"]\n[1,2,3,4]\n
# @lcpr case=end

#
