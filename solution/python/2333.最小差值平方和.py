"""2333. 最小差值平方和"""


class Solution:
    def minSumSquareDiff(
        self, nums1: list[int], nums2: list[int], k1: int, k2: int
    ) -> int:
        differences = sorted((abs(a - b) for a, b in zip(nums1, nums2)), reverse=True)
        operations = k1 + k2
        suffix = [0] * (len(differences) + 1)
        for i in range(len(differences) - 1, -1, -1):
            suffix[i] = suffix[i + 1] + differences[i] * differences[i]
        for i, value in enumerate(differences):
            width = i + 1
            next_value = differences[i + 1] if i + 1 < len(differences) else 0
            cost = (value - next_value) * width
            if operations >= cost:
                operations -= cost
            else:
                quotient, remainder = divmod(operations, width)
                level = value - quotient
                return (
                    suffix[i + 1]
                    + (width - remainder) * level * level
                    + remainder * (level - 1) * (level - 1)
                )
        return 0

if __name__ == "__main__":
    assert Solution().minSumSquareDiff([1,4,10,12],[5,8,6,9],1,1) == 43
