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
