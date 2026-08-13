from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next=None):
        self.val = val
        self.next = next


class Solution:
    def frequenciesOfElements(self, head: Optional[ListNode]) -> Optional[ListNode]:
        counts = {}
        cur = head
        while cur:
            counts[cur.val] = counts.get(cur.val, 0) + 1
            cur = cur.next
        dummy = ListNode()
        tail = dummy
        for count in counts.values():
            tail.next = ListNode(count)
            tail = tail.next
        return dummy.next


if __name__ == "__main__":
    test_cases = [([1, 1, 2, 3, 3, 3], [2, 1, 3])]
    for _, (values, expected) in enumerate(test_cases):
        dummy = ListNode()
        tail = dummy
        for value in values:
            tail.next = ListNode(value)
            tail = tail.next
        node = Solution().frequenciesOfElements(dummy.next)
        actual = []
        while node:
            actual.append(node.val)
            node = node.next
        assert actual == expected
