"""2574. 左 and 右数组的和"""


class Solution:
    def leftRightDifference(self, nums: list[int]) -> list[int]:
        right = sum(nums)
        left = 0
        answer = []
        for number in nums:
            right -= number
            answer.append(abs(left - right))
            left += number
        return answer


if __name__ == "__main__":
    test_cases = [(([10, 4, 8, 3],), [15, 1, 11, 22])]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().leftRightDifference(*args) == expected
