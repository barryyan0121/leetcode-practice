"""2186. 制造有效分配的最少组数"""

from collections import Counter


class Solution:
    def minGroupsForValidAssignment(self, nums: list[int]) -> int:
        frequencies = Counter(nums).values()
        minimum = min(frequencies)
        for group_size in range(minimum, 0, -1):
            groups = 0
            for frequency in frequencies:
                low = (frequency + group_size) // (group_size + 1)
                high = frequency // group_size
                if low > high:
                    break
                groups += low
            else:
                return groups
        return len(nums)


if __name__ == "__main__":
    assert Solution().minGroupsForValidAssignment([3, 2, 3, 2, 3]) == 2
