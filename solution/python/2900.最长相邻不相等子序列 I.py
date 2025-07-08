#
# @lc app=leetcode.cn id=2900 lang=python3
# @lcpr version=30201
#
# [2900] 最长相邻不相等子序列 I
#
from typing import List


# @lc code=start
class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        ans = []
        for i in range(len(words)):
            if i == 0 or groups[i] != groups[i - 1]:
                ans.append(words[i])
        return ans


# @lc code=end


#
# @lcpr case=start
# ["e","a","b"]\n[0,0,1]\n
# @lcpr case=end

# @lcpr case=start
# ["a","b","c","d"]\n[1,0,1,1]\n
# @lcpr case=end

#
