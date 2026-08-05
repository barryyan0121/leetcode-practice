"""2573. 找出对应 LCP 矩阵的字符串"""


class Solution:
    def findTheString(self, lcp: list[list[int]]) -> str:
        n = len(lcp)
        answer = [""] * n
        next_char = ord("a")
        for index in range(n):
            if answer[index]:
                continue
            if next_char > ord("z"):
                return ""
            for other in range(index, n):
                if lcp[index][other] > 0:
                    answer[other] = chr(next_char)
            next_char += 1
        common = [[0] * (n + 1) for _ in range(n + 1)]
        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                common[i][j] = 1 + common[i + 1][j + 1] if answer[i] == answer[j] else 0
                if common[i][j] != lcp[i][j]:
                    return ""
        return "".join(answer)


if __name__ == "__main__":
    test_cases = [(([[4, 0, 2, 0], [0, 3, 0, 1], [2, 0, 2, 0], [0, 1, 0, 1]],), "abab")]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().findTheString(*args) == expected
