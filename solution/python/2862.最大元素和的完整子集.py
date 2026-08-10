"""2862. 最大元素和的完整子集"""


class Solution:
    def maximumSum(self, nums: list[int]) -> int:
        groups = {}
        for index, value in enumerate(nums, 1):
            number, kernel, factor = index, 1, 2
            while factor * factor <= number:
                exponent = 0
                while number % factor == 0:
                    number //= factor
                    exponent ^= 1
                if exponent:
                    kernel *= factor
                factor += 1
            if number > 1:
                kernel *= number
            groups[kernel] = groups.get(kernel, 0) + value
        return max(groups.values())


if __name__ == "__main__":
    assert Solution().maximumSum([8, 7, 3, 5, 7, 2, 4, 6]) == 13
