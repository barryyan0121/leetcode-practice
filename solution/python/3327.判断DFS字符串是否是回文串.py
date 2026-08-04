class Solution:
    def findAnswer(self, parent: list[int], s: str) -> list[bool]:
        n = len(parent)
        children = [[] for _ in range(n)]
        for node in range(1, n):
            children[parent[node]].append(node)

        starts = [0] * n
        ends = [0] * n
        order = []
        stack = [(0, False)]
        while stack:
            node, visited = stack.pop()
            if visited:
                starts[node] = (
                    starts[children[node][0]] if children[node] else len(order)
                )
                order.append(s[node])
                ends[node] = len(order)
            else:
                stack.append((node, True))
                for child in reversed(children[node]):
                    stack.append((child, False))

        d1 = [0] * n
        left = right = 0
        for index in range(n):
            radius = (
                1 if index > right else min(d1[left + right - index], right - index + 1)
            )
            while (
                index - radius >= 0
                and index + radius < n
                and order[index - radius] == order[index + radius]
            ):
                radius += 1
            d1[index] = radius
            if index + radius - 1 > right:
                left, right = index - radius + 1, index + radius - 1

        d2 = [0] * n
        left = 0
        right = -1
        for index in range(n):
            radius = (
                0
                if index > right
                else min(d2[left + right - index + 1], right - index + 1)
            )
            while (
                index - radius - 1 >= 0
                and index + radius < n
                and order[index - radius - 1] == order[index + radius]
            ):
                radius += 1
            d2[index] = radius
            if index + radius - 1 > right:
                left, right = index - radius, index + radius - 1

        answer = []
        for start, end in zip(starts, ends):
            length = end - start
            if length % 2:
                center = (start + end - 1) // 2
                answer.append(d1[center] >= length // 2 + 1)
            else:
                center = (start + end) // 2
                answer.append(d2[center] >= length // 2)
        return answer


if __name__ == "__main__":
    test_cases = [
        (([-1, 0, 0, 1, 1, 2], "aababa"), [True, True, False, True, True, True]),
        (([-1, 0, 0, 0, 0], "aabcb"), [True, True, True, True, True]),
    ]
    for _, ((parent, s), expected) in enumerate(test_cases):
        assert Solution().findAnswer(parent, s) == expected
