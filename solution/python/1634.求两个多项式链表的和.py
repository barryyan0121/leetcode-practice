from typing import Optional


class PolyNode:
    def __init__(self, coefficient, power, next_node=None):
        self.coefficient = coefficient
        self.power = power
        self.next = next_node


class Solution:
    def addPoly(self, poly1: "PolyNode", poly2: "PolyNode") -> "PolyNode":
        dummy = PolyNode(0, 0)
        tail = dummy
        while poly1 or poly2:
            if poly2 is None or (poly1 and poly1.power > poly2.power):
                coefficient, power = poly1.coefficient, poly1.power
                poly1 = poly1.next
            elif poly1 is None or poly2.power > poly1.power:
                coefficient, power = poly2.coefficient, poly2.power
                poly2 = poly2.next
            else:
                coefficient, power = poly1.coefficient + poly2.coefficient, poly1.power
                poly1, poly2 = poly1.next, poly2.next
            if coefficient:
                tail.next = PolyNode(coefficient, power)
                tail = tail.next
        return dummy.next


if __name__ == "__main__":
    def chain(items):
        head = tail = None
        for coefficient, power in items:
            node = PolyNode(coefficient, power)
            if head is None:
                head = tail = node
            else:
                tail.next = node
                tail = node
        return head

    out = Solution().addPoly(chain([(1, 2), (2, 1)]), chain([(3, 2), (-2, 1), (4, 0)]))
    assert [(out.coefficient, out.power), (out.next.coefficient, out.next.power)] == [(4, 2), (4, 0)]
