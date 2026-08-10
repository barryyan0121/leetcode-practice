"""2265. 统计值等于子树平均值的节点数"""


class Solution:
    def averageOfSubtree(self, root) -> int:
        answer = 0

        def dfs(node):
            nonlocal answer
            if not node:
                return 0, 0
            left_sum, left_count = dfs(node.left)
            right_sum, right_count = dfs(node.right)
            total = left_sum + right_sum + node.val
            count = left_count + right_count + 1
            answer += total // count == node.val
            return total, count

        dfs(root)
        return answer
