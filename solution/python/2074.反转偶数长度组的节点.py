"""2074. 反转偶数长度组的节点"""


class Solution:
    def reverseEvenLengthGroups(self, head):
        nodes = []
        current = head
        while current:
            nodes.append(current)
            current = current.next
        start = 0
        group_size = 1
        while start < len(nodes):
            end = min(start + group_size, len(nodes))
            if (end - start) % 2 == 0:
                nodes[start:end] = reversed(nodes[start:end])
            start = end
            group_size += 1
        for first, second in zip(nodes, nodes[1:]):
            first.next = second
        if nodes:
            nodes[-1].next = None
        return nodes[0] if nodes else None


if __name__ == "__main__":
    test_cases = [(None, None)]
    for _, (head, expected) in enumerate(test_cases):
        assert Solution().reverseEvenLengthGroups(head) == expected
