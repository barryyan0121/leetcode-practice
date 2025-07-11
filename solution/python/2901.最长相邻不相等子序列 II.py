#
# @lc app=leetcode.cn id=2901 lang=python3
# @lcpr version=30201
#
# [2901] 最长相邻不相等子序列 II
#


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


#
# @lcpr case=start
# 3\n["bab","dab","cab"]\n[1,2,2]\n
# @lcpr case=end

# @lcpr case=start
# 4\n["a","b","c","d"]\n[1,2,3,4]\n
# @lcpr case=end

#
