"""2471. 逐层排序二叉树所需的最少操作数目"""


class Solution:
    def minimumOperations(self, root) -> int:
        answer = 0
        level = [root]
        while level:
            values = [node.val for node in level]
            target = sorted(values)
            positions = {value: index for index, value in enumerate(values)}
            for index, value in enumerate(target):
                if values[index] == value:
                    continue
                other = positions[value]
                positions[values[index]] = other
                values[index], values[other] = values[other], values[index]
                answer += 1
            level = [
                child for node in level for child in (node.left, node.right) if child
            ]
        return answer


if __name__ == "__main__":

    class Node:
        def __init__(self, val, left=None, right=None):
            self.val, self.left, self.right = val, left, right

    assert (
        Solution().minimumOperations(
            Node(1, Node(3, Node(7), Node(6)), Node(2, Node(5), Node(4)))
        )
        == 3
    )
