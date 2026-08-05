class Solution:
    def doubleIt(self, head: "ListNode") -> "ListNode":
        values = []
        while head:
            values.append(head)
            head = head.next
        carry = 0
        for node in reversed(values):
            total = node.val * 2 + carry
            node.val, carry = total % 10, total // 10
        if carry:
            node = type(values[0])(carry)
            node.next = values[0]
            return node
        return values[0]


if __name__ == "__main__":
    print("链表题，跳过本地模拟")
