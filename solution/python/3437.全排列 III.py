class Solution:
    def permute(self, n: int) -> list[list[int]]:
        answer = []
        path = []
        used = [False] * (n + 1)

        def dfs() -> None:
            if len(path) == n:
                answer.append(path[:])
                return
            for value in range(1, n + 1):
                if not used[value] and (not path or path[-1] % 2 != value % 2):
                    used[value] = True
                    path.append(value)
                    dfs()
                    path.pop()
                    used[value] = False

        dfs()
        return answer


if __name__ == "__main__":
    test_cases = [
        ((3,), [[1, 2, 3], [3, 2, 1]]),
    ]
    for _, ((n,), expected) in enumerate(test_cases):
        assert Solution().permute(n) == expected
