class Solution:
    def checkArray(self, nums: list[int], k: int) -> bool:
        active = 0
        diff = [0] * (len(nums) + 1)
        for i, value in enumerate(nums):
            active += diff[i]
            value += active
            if value < 0 or (value and i + k > len(nums)):
                return False
            if value:
                active -= value
                diff[i + k] += value
        return True


if __name__ == "__main__":
    assert Solution().checkArray([2, 2, 3, 1, 1, 0], 3) is True
