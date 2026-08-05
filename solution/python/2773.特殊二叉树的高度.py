class Solution:
    def heightOfTree(self, root: "TreeNode") -> int:
        if not root:
            return -1
        if root.left is not None and root.right is not None and root.left.right is root:
            return 0
        return 1 + max(self.heightOfTree(root.left), self.heightOfTree(root.right))


if __name__ == "__main__":
    print("交互题，跳过本地模拟")
