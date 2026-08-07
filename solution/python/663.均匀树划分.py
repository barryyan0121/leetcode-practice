#
# @lc app=leetcode.cn id=663 lang=python3
#
# [663] 均匀树划分
#


# @lc code=start
class Solution:
    def checkEqualTree(self, root) -> bool:
        sums = []

        def total(node):
            if not node:
                return 0
            value = node.val + total(node.left) + total(node.right)
            sums.append(value)
            return value

        whole = total(root)
        if whole % 2:
            return False
        target = whole // 2
        return sums.count(target) > (1 if target == 0 else 0)


# @lc code=end
