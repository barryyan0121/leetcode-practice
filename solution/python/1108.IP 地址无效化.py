#
# @lc app=leetcode.cn id=1108 lang=python3
# @lcpr version=30201
#
# [1108] IP 地址无效化
#

# @lc code=start
class Solution:
    def defangIPaddr(self, address: str) -> str:
        res = ""
        for letter in address:
            if letter == ".":
                res += "[.]"
            else:
                res += letter
        return res
# @lc code=end



#
# @lcpr case=start
# "1.1.1.1"\n
# @lcpr case=end

# @lcpr case=start
# "255.100.50.0"\n
# @lcpr case=end

#

