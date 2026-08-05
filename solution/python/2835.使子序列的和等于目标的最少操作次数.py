class Solution:
    def minOperations(self, nums: list[int], target: int) -> int:
        counts = [0] * 32
        for value in nums:
            counts[value.bit_length() - 1] += 1
        ans = 0
        for bit in range(31):
            if target >> bit & 1:
                if counts[bit]:
                    counts[bit] -= 1
                else:
                    j = bit + 1
                    while j < 31 and not counts[j]:
                        j += 1
                    if j == 31:
                        return -1
                    while j > bit:
                        counts[j] -= 1
                        counts[j - 1] += 2
                        ans += 1
                        j -= 1
                    counts[bit] -= 1
            counts[bit + 1] += counts[bit] // 2
        return ans


if __name__ == "__main__":
    assert Solution().minOperations([1, 2, 8], 7) == 1
