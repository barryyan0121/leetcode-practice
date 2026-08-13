"""2487. 从链表中移除节点"""


class Solution:
    def removeNodes(self, head):
        stack = []
        node = head
        while node:
            while stack and stack[-1].val < node.val:
                stack.pop()
            stack.append(node)
            node = node.next
        for index in range(len(stack) - 1):
            stack[index].next = stack[index + 1]
        stack[-1].next = None
        return stack[0]

if __name__ == "__main__":
    class Node:
        def __init__(self, val, next_node=None): self.val, self.next = val, next_node
    head = Node(5, Node(2, Node(13, Node(3, Node(8)))))
    result = Solution().removeNodes(head)
    assert result.val == 13 and result.next.val == 8
