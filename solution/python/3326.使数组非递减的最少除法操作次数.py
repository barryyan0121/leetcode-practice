class Solution:
    def minOperations(self, nums: list[int]) -> int:
        operations = 0
        for index in range(len(nums) - 2, -1, -1):
            if nums[index] <= nums[index + 1]:
                continue
            value = nums[index]
            divisor = 2
            while value % divisor:
                divisor += 1
            smallest_prime = divisor
            if smallest_prime > nums[index + 1]:
                return -1
            nums[index] = smallest_prime
            operations += 1
        return operations


if __name__ == "__main__":
    test_cases = [
        (([25, 7],), 1),
        (([7, 7, 6],), -1),
        (([1, 1, 1, 1],), 0),
    ]
    for _, ((nums,), expected) in enumerate(test_cases):
        assert Solution().minOperations(nums) == expected
