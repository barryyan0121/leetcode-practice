"""2046. 给按照绝对值排序的链表排序"""


class ListNode:
    def __init__(self, val=0, next_node=None):
        self.val = val
        self.next = next_node


class Solution:
    def sortLinkedList(self, head):
        negative = None
        positive = head
        while positive:
            if positive.val < 0:
                node = positive
                positive = positive.next
                node.next = negative
                negative = node
            else:
                break
        if negative is None:
            return head
        tail = negative
        while tail.next:
            tail = tail.next
        tail.next = positive
        return negative


if __name__ == "__main__":
    head = ListNode(-5, ListNode(-2, ListNode(0, ListNode(3))))
    result = Solution().sortLinkedList(head)
    values = []
    while result:
        values.append(result.val)
        result = result.next
    test_cases = [(([-5, -2, 0, 3],), [-2, -5, 0, 3])]
    for _, (args, expected) in enumerate(test_cases):
        assert values == expected
