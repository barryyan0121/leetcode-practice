from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        sums = {0: dummy}
        total = 0
        node = dummy.next
        while node:
            total += node.val
            sums[total] = node
            node = node.next
        total = 0
        node = dummy
        while node:
            total += node.val
            node.next = sums[total].next
            node = node.next
        return dummy.next


if __name__ == "__main__":
    test_cases = [
        (ListNode(1, ListNode(2, ListNode(-3, ListNode(3, ListNode(1))))), [3, 1])
    ]
    for _, (head, expected) in enumerate(test_cases):
        result = Solution().removeZeroSumSublists(head)
        values = []
        while result:
            values.append(result.val)
            result = result.next
        assert values == expected
