class Solution:
    def sumOfGoodSubsequences(self, nums: list[int]) -> int:
        modulo = 10**9 + 7
        count = {}
        total = {}
        answer = 0
        for value in nums:
            new_count = 1 + count.get(value - 1, 0) + count.get(value + 1, 0)
            new_total = (
                value * new_count + total.get(value - 1, 0) + total.get(value + 1, 0)
            ) % modulo
            count[value] = (count.get(value, 0) + new_count) % modulo
            total[value] = (total.get(value, 0) + new_total) % modulo
            answer = (answer + new_total) % modulo
        return answer


if __name__ == "__main__":
    test_cases = [
        (([1, 2, 1],), 14),
        (([3, 4, 5],), 40),
        (([1],), 1),
    ]
    for _, ((nums,), expected) in enumerate(test_cases):
        assert Solution().sumOfGoodSubsequences(nums) == expected
