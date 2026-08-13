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


if __name__ == "__main__":

    class TreeNode:
        def __init__(self, val=0, left=None, right=None):
            self.val, self.left, self.right = val, left, right

    root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(6))
    left, right = Solution().splitBST(root, 2)
    assert left.val == 2 and left.left.val == 1 and left.right is None
    assert right.val == 4 and right.right.val == 6
