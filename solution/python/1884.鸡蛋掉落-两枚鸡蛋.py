"""1884. 鸡蛋掉落-两枚鸡蛋"""


class Solution:
    def twoEggDrop(self, n: int) -> int:
        steps = 0
        floors = 0
        while floors < n:
            steps += 1
            floors += steps
        return steps


if __name__ == "__main__":
    test_cases = [(2, 2), (100, 14)]
    for _, (n, expected) in enumerate(test_cases):
        assert Solution().twoEggDrop(n) == expected
