"""2191. 将杂乱无章的数字排序"""


class Solution:
    def sortJumbled(self, mapping: list[int], nums: list[int]) -> list[int]:
        def mapped(value: int) -> int:
            if value == 0:
                return mapping[0]
            digits = []
            while value:
                digits.append(mapping[value % 10])
                value //= 10
            result = 0
            for digit in reversed(digits):
                result = result * 10 + digit
            return result

        return sorted(nums, key=mapped)


if __name__ == "__main__":
    assert Solution().sortJumbled([8, 9, 4, 0, 2, 1, 3, 5, 7, 6], [991, 338, 38]) == [
        338,
        38,
        991,
    ]
