class Solution:
    def maximumBeauty(self, flowers):
        best, first, prefix = -(10**18), {}, 0
        for value in flowers:
            if value in first:
                best = max(best, prefix + first[value])
            else:
                first[value] = 2 * value - prefix - max(0, value)
            prefix += max(0, value)
        return best


if __name__ == "__main__":
    assert Solution().maximumBeauty([1, -1, 2, 2]) == 4
