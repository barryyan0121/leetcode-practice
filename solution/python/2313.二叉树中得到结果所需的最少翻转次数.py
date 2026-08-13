class Solution:
    def minimumFlips(self, root, result):
        def dfs(node):
            if node.val < 2:
                return (node.val != 0, node.val != 1)
            if node.val == 5:
                a = dfs(node.left or node.right)
                return a[1], a[0]
            a = dfs(node.left)
            b = dfs(node.right)
            vals = [(a[x] + b[y]) for x in range(2) for y in range(2)]
            if node.val == 2:
                return (vals[0], min(vals[1:]))
            if node.val == 3:
                return (min(vals[:3]), vals[3])
            return min(vals[0], vals[3]), min(vals[1], vals[2])

        x = dfs(root)
        return int(x[result])


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


if __name__ == "__main__":
    test_cases = [
        (TreeNode(2, TreeNode(1), TreeNode(0)), True, 0),
        (TreeNode(5, TreeNode(0)), True, 0),
        (TreeNode(4, TreeNode(1), TreeNode(0)), True, 0),
    ]
    for index, (root, result, expected) in enumerate(test_cases):
        assert Solution().minimumFlips(root, result) == expected, index
