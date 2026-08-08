from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteNodes(
        self, head: Optional[ListNode], m: int, n: int
    ) -> Optional[ListNode]:
        node = head
        while node:
            for _ in range(m - 1):
                if not node.next:
                    return head
                node = node.next
            next_node = node.next
            for _ in range(n):
                if not next_node:
                    break
                next_node = next_node.next
            node.next = next_node
            node = next_node
        return head


if __name__ == "__main__":
    test_cases = [
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], 2, 3, [1, 2, 6, 7, 11, 12]),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], 1, 3, [1, 5, 9]),
    ]
    for _, (values, m, n, expected) in enumerate(test_cases):
        dummy = ListNode()
        tail = dummy
        for value in values:
            tail.next = ListNode(value)
            tail = tail.next
        node = Solution().deleteNodes(dummy.next, m, n)
        result = []
        while node:
            result.append(node.val)
            node = node.next
        assert result == expected
