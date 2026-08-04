class Solution:
    def minDifference(self, nums: list[int]) -> int:
        maximum_gap = 0
        boundary_values = []
        for index in range(1, len(nums)):
            left, right = nums[index - 1], nums[index]
            if left == -1 or right == -1:
                if left != -1:
                    boundary_values.append(left)
                if right != -1:
                    boundary_values.append(right)
            else:
                maximum_gap = max(maximum_gap, abs(left - right))

        if not boundary_values:
            return maximum_gap
        low = maximum_gap
        high = (max(boundary_values) - min(boundary_values) + 1) // 2

        def possible(limit: int, x: int, y: int) -> bool:
            index = 0
            while index < len(nums):
                if nums[index] != -1:
                    index += 1
                    continue
                start = index
                while index < len(nums) and nums[index] == -1:
                    index += 1
                length = index - start
                left = nums[start - 1] if start else None
                right = nums[index] if index < len(nums) else None
                if left is None and right is None:
                    continue
                if left is None:
                    if min(abs(right - x), abs(right - y)) > limit:
                        return False
                elif right is None:
                    if min(abs(left - x), abs(left - y)) > limit:
                        return False
                elif length == 1:
                    if (
                        min(
                            max(abs(left - x), abs(right - x)),
                            max(abs(left - y), abs(right - y)),
                        )
                        > limit
                    ):
                        return False
                else:
                    options = (
                        max(abs(left - x), abs(right - x)),
                        max(abs(left - y), abs(right - y)),
                        max(abs(left - x), abs(x - y), abs(right - y)),
                        max(abs(left - y), abs(x - y), abs(right - x)),
                    )
                    if min(options) > limit:
                        return False
            return True

        while low < high:
            middle = (low + high) // 2
            minimum = min(boundary_values) + middle
            maximum = max(boundary_values) - middle
            if possible(middle, minimum, maximum):
                high = middle
            else:
                low = middle + 1
        return low


if __name__ == "__main__":
    test_cases = [
        (([1, 2, -1, 10, 8],), 4),
        (([-1, -1, -1],), 0),
        (([1, -1, 10],), 5),
    ]
    for _, ((nums,), expected) in enumerate(test_cases):
        assert Solution().minDifference(nums) == expected
