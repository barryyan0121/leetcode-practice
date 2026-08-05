"""2426. 满足不等式的数对数目"""

from bisect import bisect_left, bisect_right


class Solution:
    def numberOfPairs(self, nums1: list[int], nums2: list[int], diff: int) -> int:
        values = [a - b for a, b in zip(nums1, nums2)]
        ordered = sorted(values)
        bit = [0] * (len(ordered) + 1)

        def add(index: int) -> None:
            while index < len(bit):
                bit[index] += 1
                index += index & -index

        def prefix(index: int) -> int:
            total = 0
            while index:
                total += bit[index]
                index -= index & -index
            return total

        answer = 0
        for value in values:
            threshold = value + diff
            answer += prefix(bisect_right(ordered, threshold))
            add(bisect_left(ordered, value) + 1)
        return answer


if __name__ == "__main__":
    test_cases = [(([3, 2, 5], [2, 2, 1], 1), 3)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().numberOfPairs(*args) == expected
