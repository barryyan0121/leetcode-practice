"""3062. 链表游戏的获胜者"""


class Solution:
    def gameResult(self, head) -> str:
        odd = even = 0
        index = 0
        while head:
            if index % 2:
                even += head.val
            else:
                odd += head.val
            index += 1
            head = head.next
        return "Odd" if odd > even else "Even" if even > odd else "Tie"
