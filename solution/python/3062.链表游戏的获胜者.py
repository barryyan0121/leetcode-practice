"""3062. 链表游戏的获胜者"""


class Solution:
    def gameResult(self, head) -> str:
        odd = even = 0
        index = 1
        while head:
            if index % 2:
                odd += head.val
            else:
                even += head.val
            index += 1
            head = head.next
        return "Odd" if odd > even else "Even" if even > odd else "Tie"


if __name__ == "__main__":

    class ListNode:
        def __init__(self, val=0, next=None):
            self.val = val
            self.next = next

    def build(values):
        head = None
        for value in reversed(values):
            head = ListNode(value, head)
        return head

    s = Solution()

    def expected(values):
        odd = sum(values[0::2])
        even = sum(values[1::2])
        return "Odd" if odd > even else "Even" if even > odd else "Tie"

    for values in ([2, 1], [2, 5, 4, 7, 20, 5], [1]):
        assert s.gameResult(build(values)) == expected(values)
    print("3062 ok")
