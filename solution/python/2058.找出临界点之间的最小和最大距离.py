"""2058. 找出临界点之间的最小和最大距离"""


class Solution:
    def nodesBetweenCriticalPoints(self, head):
        first = previous_critical = -1
        minimum = float("inf")
        previous = head
        index = 1
        while previous and previous.next:
            current = previous.next
            if (
                current.next
                and current.val < previous.val
                and current.val < current.next.val
            ) or (
                current.next
                and current.val > previous.val
                and current.val > current.next.val
            ):
                if first < 0:
                    first = index
                if previous_critical >= 0:
                    minimum = min(minimum, index - previous_critical)
                previous_critical = index
            previous = current
            index += 1
        if first < 0 or first == previous_critical:
            return [-1, -1]
        return [minimum, previous_critical - first]


if __name__ == "__main__":
    test_cases = [([], [-1, -1])]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().nodesBetweenCriticalPoints(None) == expected
