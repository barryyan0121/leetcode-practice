"""3032. 统计范围内的数字个数"""


class Solution:
    def numberCount(self, a: int, b: int) -> int:
        return sum(
            len(set(str(number))) == len(str(number)) for number in range(a, b + 1)
        )


if __name__ == "__main__":
    assert Solution().numberCount(1, 20) == 19
