"""2074. 反转偶数长度组的节点"""


class Solution:
    def reverseEvenLengthGroups(self, head):
        previous = head
        group_size = 1
        while previous and previous.next:
            group_start = previous.next
            node = group_start
            length = 0
            while node and length < group_size:
                node = node.next
                length += 1
            if length % 2 == 0:
                before, current = previous, group_start
                for _ in range(length):
                    next_node = current.next
                    current.next = before
                    before, current = current, next_node
                previous.next = before
                group_start.next = current
                previous = group_start
            else:
                for _ in range(length):
                    previous = previous.next
            group_size += 1
        return head


if __name__ == "__main__":
    test_cases = [(None, None)]
    for _, (head, expected) in enumerate(test_cases):
        assert Solution().reverseEvenLengthGroups(head) == expected
