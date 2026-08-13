from typing import Optional


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
