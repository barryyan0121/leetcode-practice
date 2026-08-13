"""2196. 根据描述创建二叉树"""


class Solution:
    def createBinaryTree(self, descriptions: list[list[int]]):
        nodes = {}
        children = set()
        for parent, child, is_left in descriptions:
            nodes.setdefault(parent, TreeNode(parent))
            nodes.setdefault(child, TreeNode(child))
            if is_left:
                nodes[parent].left = nodes[child]
            else:
                nodes[parent].right = nodes[child]
            children.add(child)
        return nodes[next(value for value in nodes if value not in children)]


if __name__ == "__main__":

    class TreeNode:
        def __init__(self, val=0, left=None, right=None):
            self.val, self.left, self.right = val, left, right

    root = Solution().createBinaryTree([[20, 15, 1], [20, 17, 0], [15, 10, 1]])
    assert root.val == 20 and root.left.val == 15 and root.right.val == 17
