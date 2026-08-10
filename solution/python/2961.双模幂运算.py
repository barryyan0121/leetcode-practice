"""2961. 双模幂运算"""


class Solution:
    def getGoodIndices(self, variables: list[list[int]], target: int) -> list[int]:
        return [
            index
            for index, (a, b, c, m) in enumerate(variables)
            if pow(pow(a, b, 10), c, m) == target
        ]


if __name__ == "__main__":
    assert Solution().getGoodIndices([[2, 3, 3, 10], [3, 3, 3, 10]], 2) == [0]
