class Solution:
    def printLinkedListInReverse(self, head: "ImmutableListNode") -> None:
        nodes = []
        while head:
            nodes.append(head)
            head = head.getNext()
        for node in reversed(nodes):
            node.printValue()


if __name__ == "__main__":

    class ImmutableListNode:
        output = []

        def __init__(self, value, next_node=None):
            self.value = value
            self.next_node = next_node

        def getNext(self):
            return self.next_node

        def printValue(self):
            self.output.append(self.value)

    test_cases = [(ImmutableListNode(1, ImmutableListNode(2)), [2, 1])]
    for _, (head, expected) in enumerate(test_cases):
        ImmutableListNode.output = []
        Solution().printLinkedListInReverse(head)
        assert ImmutableListNode.output == expected
