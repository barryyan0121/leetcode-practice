"""2181. 合并零之间的节点"""


class Solution:
    def mergeNodes(self, head):
        write = head
        read = head.next
        total = 0
        while read:
            if read.val == 0:
                write.val = total
                total = 0
                if read.next:
                    write.next = read.next
                    write = write.next
                else:
                    write.next = None
            else:
                total += read.val
            read = read.next
        write.next = None
        return head


if __name__ == "__main__":

    class Node:
        def __init__(self, val, next=None):
            self.val, self.next = val, next

    head = Node(0, Node(3, Node(1, Node(0))))
    assert Solution().mergeNodes(head).val == 4
