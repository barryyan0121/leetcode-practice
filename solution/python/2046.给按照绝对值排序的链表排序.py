"""2046. 给按照绝对值排序的链表排序"""


class Solution:
    def sortLinkedList(self, head):
        negative = []
        positive = []
        node = head
        while node:
            (negative if node.val < 0 else positive).append(node)
            node = node.next
        ordered = negative[::-1] + positive
        for first, second in zip(ordered, ordered[1:]):
            first.next = second
        if ordered:
            ordered[-1].next = None
        return ordered[0] if ordered else None


test_cases = [([-1, 2, -3, 4], [-3, -1, 2, 4])]


if __name__ == "__main__":

    class Node:
        def __init__(self, val, next=None):
            self.val, self.next = val, next

    head = Node(-1, Node(2, Node(-3, Node(4))))
    result = Solution().sortLinkedList(head)
    assert [
        result.val,
        result.next.val,
        result.next.next.val,
        result.next.next.next.val,
    ] == [-3, -1, 2, 4]
    for index, (values, expected) in enumerate(test_cases):
        assert index == 0
        assert expected == [-3, -1, 2, 4]
