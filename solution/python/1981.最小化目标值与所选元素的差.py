"""1981. 最小化目标值与所选元素的差"""


class Solution:
    def minimizeTheDifference(self, mat: list[list[int]], target: int) -> int:
        possible = {0}
        for row in mat:
            possible = {total + value for total in possible for value in row}
        return min(abs(total - target) for total in possible)


if __name__ == "__main__":
    test_cases = [(([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 13), 0)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().minimizeTheDifference(*args) == expected
