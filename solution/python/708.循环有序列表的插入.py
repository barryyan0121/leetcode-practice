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
