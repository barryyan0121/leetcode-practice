#
# @lc app=leetcode.cn id=708 lang=python3
#
# [708] 循环有序列表的插入
#


# @lc code=start
class Solution:
    def insert(self, head, insertVal: int):
        node = Node(insertVal)
        if head is None:
            node.next = node
            return node
        current = head
        while True:
            next_node = current.next
            in_order = current.val <= insertVal <= next_node.val
            at_turn = current.val > next_node.val and (
                insertVal >= current.val or insertVal <= next_node.val
            )
            if in_order or at_turn or next_node is head:
                node.next = next_node
                current.next = node
                return head
            current = next_node


# @lc code=end

if __name__ == "__main__":

    class Node:
        def __init__(self, val, next_node=None):
            self.val, self.next = val, next_node

    node = Node(3)
    node.next = node
    head = Solution().insert(node, 1)
    assert sorted([head.val, head.next.val]) == [1, 3]


if __name__ == "__main__":

    class Node:
        def __init__(self, val, next=None):
            self.val, self.next = val, next

    n1, n3 = Node(1), Node(3)
    n1.next = n3
    n3.next = n1
    head = Solution().insert(n1, 2)
    assert head.next.val == 2 and head.next.next.val == 3
    single = Solution().insert(None, 5)
    assert single.val == 5 and single.next is single
