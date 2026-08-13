from typing import List


class Solution:
    def rotateElements(self, nums: List[int], k: int) -> List[int]:
        indices = [i for i, value in enumerate(nums) if value >= 0]
        values = [nums[i] for i in indices]
        if values:
            values = values[k % len(values) :] + values[: k % len(values)]
            for i, value in zip(indices, values):
                nums[i] = value
        return nums


if __name__ == "__main__":
    assert Solution().rotateElements([-1, 0, 1, 2, -1, 3], 2) == [-1, 2, 3, 0, -1, 1]
