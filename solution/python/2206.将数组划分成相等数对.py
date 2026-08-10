"""2206. 将数组划分成相等数对"""

from collections import Counter


class Solution:
    def divideArray(self, nums: list[int]) -> bool:
        return all(count % 2 == 0 for count in Counter(nums).values())
