from typing import Optional

from common.node import ListNode


class Solution:
    def deleteDuplicatesUnsorted(self, head: Optional[ListNode]) -> Optional[ListNode]:
        seen = set()
        previous = None
        current = head
        while current:
            if current.val in seen:
                previous.next = current.next
            else:
                seen.add(current.val)
                previous = current
            current = current.next
        return head


if __name__ == "__main__":

    def vals(head):
        result = []
        while head:
            result.append(head.val)
            head = head.next
        return result

    head = ListNode(1, ListNode(2, ListNode(1, ListNode(3))))
    assert vals(Solution().deleteDuplicatesUnsorted(head)) == [1, 2, 3]
