class Solution:
    def minCost(self, nums: list[int]) -> int:
        xantreloqu = nums
        size = len(nums)
        if size < 3:
            return max(nums)
        cost = {
            0: max(nums[1], nums[2]),
            1: max(nums[0], nums[2]),
            2: max(nums[0], nums[1]),
        }
        position = 3
        while position + 1 < size:
            first, second = nums[position], nums[position + 1]
            updated = {}
            for retained, current in cost.items():
                updated[retained] = min(
                    updated.get(retained, 10**18) + 0,
                    current + max(first, second),
                )
                updated[position] = min(
                    updated.get(position, 10**18),
                    current + max(nums[retained], second),
                )
                updated[position + 1] = min(
                    updated.get(position + 1, 10**18),
                    current + max(nums[retained], first),
                )
            cost = updated
            position += 2
        if position < size:
            return min(
                value + max(nums[retained], nums[position])
                for retained, value in cost.items()
            )
        return min(value + nums[retained] for retained, value in cost.items())


if __name__ == "__main__":
    test_cases = [
        (([6, 2, 8, 4],), 12),
        (([2, 1, 3, 3],), 5),
        (([1, 2, 3],), 4),
        (([1],), 1),
    ]
    for _, ((nums,), expected) in enumerate(test_cases):
        assert Solution().minCost(nums) == expected
