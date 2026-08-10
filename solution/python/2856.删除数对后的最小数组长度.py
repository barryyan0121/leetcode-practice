"""2856. 删除数对后的最小数组长度"""

from collections import Counter


class Solution:
    def minLengthAfterRemovals(self, nums: list[int]) -> int:
        length = len(nums)
        most = max(Counter(nums).values())
        return max(2 * most - length, length % 2)


if __name__ == "__main__":
    assert Solution().minLengthAfterRemovals([1, 1, 2, 2, 3]) == 1
