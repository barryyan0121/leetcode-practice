"""2848. 与车辆相交的点"""


class Solution:
    def numberOfPoints(self, nums: list[list[int]]) -> int:
        covered = set()
        for start, end in nums:
            covered.update(range(start, end + 1))
        return len(covered)


if __name__ == "__main__":
    assert Solution().numberOfPoints([[3, 6], [1, 5], [4, 7]]) == 7
