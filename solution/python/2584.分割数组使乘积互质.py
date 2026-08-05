"""2584. 分割数组使乘积互质"""


class Solution:
    def findValidSplit(self, nums: list[int]) -> int:
        last = {}
        for index, value in enumerate(nums):
            factor = 2
            while factor * factor <= value:
                if value % factor == 0:
                    last[factor] = index
                    while value % factor == 0:
                        value //= factor
                factor += 1
            if value > 1:
                last[value] = index
        farthest = 0
        for index, value in enumerate(nums[:-1]):
            factor = 2
            while factor * factor <= value:
                if value % factor == 0:
                    farthest = max(farthest, last[factor])
                    while value % factor == 0:
                        value //= factor
                factor += 1
            if value > 1:
                farthest = max(farthest, last[value])
            if farthest == index:
                return index
        return -1


if __name__ == "__main__":
    test_cases = [(([4, 7, 8, 15, 3, 5],), 2)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().findValidSplit(*args) == expected
