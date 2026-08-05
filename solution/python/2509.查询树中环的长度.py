"""2509. 查询树中环的长度"""


class Solution:
    def cycleLengthQueries(self, n: int, queries: list[list[int]]) -> list[int]:
        answer = []
        for first, second in queries:
            length = 1
            while first != second:
                if first > second:
                    first //= 2
                else:
                    second //= 2
                length += 1
            answer.append(length)
        return answer


if __name__ == "__main__":
    test_cases = [((3, [[5, 3], [4, 7], [2, 3]]), [4, 5, 3])]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().cycleLengthQueries(*args) == expected
