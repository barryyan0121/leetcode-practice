#
# @lc app=leetcode.cn id=3335 lang=python3
# @lcpr version=30201
#
# [3335] 字符串转换后的长度 I
#


# @lc code=start
class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        mod = 10**9 + 7
        # 初始化字符计数数组
        cnt = [0] * 26
        for ch in s:
            cnt[ord(ch) - ord("a")] += 1

        # 进行 t 次转换
        for _ in range(t):
            nxt = [0] * 26
            nxt[0] = cnt[25]  # 更新 cnt[0]
            nxt[1] = (cnt[25] + cnt[0]) % mod  # 更新 cnt[1]
            for i in range(2, 26):  # 更新 cnt[2] 到 cnt[25]
                nxt[i] = cnt[i - 1]
            cnt = nxt  # 更新 cnt 为当前轮次的结果

        # 返回所有字符计数的总和模 mod
        return sum(cnt) % mod


# @lc code=end


#
# @lcpr case=start
# "abcyy"\n2\n
# @lcpr case=end

# @lcpr case=start
# "azbk"\n1\n
# @lcpr case=end

#
