"""1925. 统计平方和三元组的数目"""


class Solution:
    def countTriples(self, n: int) -> int:
        squares = {value * value for value in range(1, n + 1)}
        return sum(
            a * a + b * b in squares for a in range(1, n + 1) for b in range(1, n + 1)
        )


if __name__ == "__main__":
    assert Solution().countTriples(5) == 2
