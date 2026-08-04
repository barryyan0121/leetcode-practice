class Solution:
    def minBitwiseArray(self, nums: list[int]) -> list[int]:
        answer = []
        for number in nums:
            if number % 2 == 0:
                answer.append(-1)
                continue
            trailing_ones = 0
            while number & (1 << trailing_ones):
                trailing_ones += 1
            answer.append(number - (1 << (trailing_ones - 1)))
        return answer


if __name__ == "__main__":
    test_cases = [
        (([2, 3, 5, 7],), [-1, 1, 4, 3]),
        (([11, 13],), [9, 12]),
    ]
    for _, ((nums,), expected) in enumerate(test_cases):
        assert Solution().minBitwiseArray(nums) == expected
