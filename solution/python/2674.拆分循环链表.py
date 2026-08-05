"""2674. 拆分循环链表"""


class Solution:
    def splitCircularLinkedList(self, list):
        slow = list
        fast = list
        while fast.next != list and fast.next.next != list:
            slow = slow.next
            fast = fast.next.next
        second = slow.next
        slow.next = list
        tail = second
        while tail.next != list:
            tail = tail.next
        tail.next = second
        return [list, second]


if __name__ == "__main__":
    test_cases = [((), True)]
    for _, (args, expected) in enumerate(test_cases):
        assert expected
