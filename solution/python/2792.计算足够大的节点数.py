class Solution:
    def countGreatEnoughNodes(self, root: "TreeNode", k: int) -> int:
        ans = 0

        def dfs(node):
            nonlocal ans
            if not node:
                return []
            values = sorted(dfs(node.left) + dfs(node.right) + [node.val])[:k]
            if len(values) == k and node.val > values[-1]:
                ans += 1
            return values

        dfs(root)
        return ans


if __name__ == "__main__":
    print("树题，跳过本地模拟")
