class Solution:
    def gameResult(self, head) -> str:
        even = odd = 0
        while head:
            if head.val > head.next.val:
                even += 1
            else:
                odd += 1
            head = head.next.next
        return "Tie" if even == odd else ("Even" if even > odd else "Odd")


if __name__ == "__main__":

    class Node:
        def __init__(self, val, next_node=None):
            self.val = val
            self.next = next_node

    head = Node(2, Node(1, Node(4, Node(3))))
    assert Solution().gameResult(head) == "Even"
