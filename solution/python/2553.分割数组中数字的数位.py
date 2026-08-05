"""2553. 分割数组中数字的数位"""


class Solution:
    def separateDigits(self, nums: list[int]) -> list[int]:
        answer = []
        for number in nums:
            answer.extend(map(int, str(number)))
        return answer


if __name__ == "__main__":
    test_cases = [(([13, 25, 83, 77],), [1, 3, 2, 5, 8, 3, 7, 7])]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().separateDigits(*args) == expected
