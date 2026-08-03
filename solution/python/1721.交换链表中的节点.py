# @lc app=leetcode.cn id=1721 lang=python3


class Solution:
    def swapNodes(self, head, k: int):
        first = head
        for _ in range(k - 1):
            first = first.next
        left = first
        right = head
        cursor = first
        while cursor.next:
            cursor = cursor.next
            right = right.next
        left.val, right.val = right.val, left.val
        return head


if __name__ == "__main__":

    class ListNode:
        def __init__(self, val=0, next=None):
            self.val, self.next = val, next

    node = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    test_cases = [(Solution().swapNodes, (node, 2), [1, 4, 3, 2, 5])]
    for _, (func, args, expected) in enumerate(test_cases):
        result = func(*args)
        actual = [
            result.val,
            result.next.val,
            result.next.next.val,
            result.next.next.next.val,
            result.next.next.next.next.val,
        ]
        assert actual == expected
    print('第 1721 题 "交换链表中的节点" 所有测试用例通过')
