"""2261. 含最多 K 个可整除元素的子数组"""


class Solution:
    def countDistinct(self, nums: list[int], k: int, p: int) -> int:
        seen = set()
        for i in range(len(nums)):
            divisible = 0
            current = []
            for value in nums[i:]:
                divisible += value % p == 0
                if divisible > k:
                    break
                current.append(value)
                seen.add(tuple(current))
        return len(seen)

if __name__ == "__main__":
    assert Solution().countDistinct([2,3,3,2,2], 2, 2) == 11
