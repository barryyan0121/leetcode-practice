"""2190. 数组中紧跟 key 之后出现最频繁的数字"""

from collections import Counter


class Solution:
    def mostFrequent(self, nums: list[int], key: int) -> int:
        counts = Counter(
            nums[index + 1] for index, value in enumerate(nums[:-1]) if value == key
        )
        return counts.most_common(1)[0][0]


if __name__ == "__main__":
    assert Solution().mostFrequent([1, 100, 200, 1, 100], 1) == 100
