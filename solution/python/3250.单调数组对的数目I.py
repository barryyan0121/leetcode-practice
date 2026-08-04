class Solution:
    def countOfPairs(self, nums: list[int]) -> int:
        modulo = 10**9 + 7
        maximum = max(nums)
        previous = [1 if value <= nums[0] else 0 for value in range(maximum + 1)]
        for current, previous_sum in zip(nums[1:], nums):
            prefix = [0] * (maximum + 1)
            running = 0
            for value in range(maximum + 1):
                running = (running + previous[value]) % modulo
                prefix[value] = running
            next_row = [0] * (maximum + 1)
            for value in range(current + 1):
                limit = min(value, value + previous_sum - current)
                if limit >= 0:
                    next_row[value] = prefix[limit]
            previous = next_row
        return sum(previous) % modulo


if __name__ == "__main__":
    test_cases = [(([2, 3, 2],), 4), (([5, 5, 5, 5],), 126)]
    for _, ((nums,), expected) in enumerate(test_cases):
        assert Solution().countOfPairs(nums) == expected
