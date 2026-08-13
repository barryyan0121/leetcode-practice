"""2358. 分组的最大数量"""


class Solution:
    def maximumGroups(self, grades: list[int]) -> int:
        groups = 0
        used = 0
        while used + groups + 1 <= len(grades):
            groups += 1
            used += groups
        return groups

if __name__ == "__main__":
    assert Solution().maximumGroups([10,6,12,7,3,5]) == 3
