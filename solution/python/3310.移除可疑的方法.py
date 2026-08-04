class Solution:
    def remainingMethods(
        self, n: int, k: int, invocations: list[list[int]]
    ) -> list[int]:
        graph = [[] for _ in range(n)]
        for caller, callee in invocations:
            graph[caller].append(callee)

        suspicious = {k}
        stack = [k]
        while stack:
            method = stack.pop()
            for callee in graph[method]:
                if callee not in suspicious:
                    suspicious.add(callee)
                    stack.append(callee)

        for caller, callee in invocations:
            if caller not in suspicious and callee in suspicious:
                return list(range(n))
        return [method for method in range(n) if method not in suspicious]


if __name__ == "__main__":
    test_cases = [
        ((4, 1, [[1, 2], [0, 1], [3, 2]]), [0, 1, 2, 3]),
        ((5, 0, [[1, 2], [0, 2], [0, 1], [3, 4]]), [3, 4]),
        ((3, 2, [[1, 2], [0, 1], [2, 0]]), []),
    ]
    for _, ((n, k, invocations), expected) in enumerate(test_cases):
        assert Solution().remainingMethods(n, k, invocations) == expected
