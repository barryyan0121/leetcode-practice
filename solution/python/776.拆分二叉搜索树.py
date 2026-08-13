"""776. 拆分二叉搜索树"""


class Solution:
    def splitBST(self, root: "TreeNode | None", target: int) -> list:
        if root is None:
            return [None, None]
        if root.val <= target:
            right_low, right_high = self.splitBST(root.right, target)
            root.right = right_low
            return [root, right_high]
        left_low, left_high = self.splitBST(root.left, target)
        root.left = left_high
        return [left_low, root]
