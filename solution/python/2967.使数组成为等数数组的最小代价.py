class Solution:
    def minimumCost(self, nums: list[int]) -> int:
        nums.sort()
        median = nums[(len(nums) - 1) // 2]
        length = len(str(median))
        half = (length + 1) // 2
        prefix = int(str(median)[:half])
        candidates = []
        for value in (prefix - 1, prefix, prefix + 1):
            if len(str(value)) < half:
                candidate = 10 ** (length - 1) - 1
            elif len(str(value)) > half:
                candidate = 10**length + 1
            else:
                left = str(value)
                candidate = int(left + (left[:-1] if length % 2 else left)[::-1])
            if candidate > 0:
                candidates.append(candidate)
        return min(
            sum(abs(value - candidate) for value in nums) for candidate in candidates
        )


if __name__ == "__main__":
    solution = Solution()
    assert solution.minimumCost([1, 2, 3, 4, 5]) == 6
    assert solution.minimumCost([10, 12, 13, 14, 15]) == 11
    assert solution.minimumCost([22, 33, 22, 33, 22]) == 22
