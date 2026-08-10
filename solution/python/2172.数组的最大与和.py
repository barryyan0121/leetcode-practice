"""2172. 数组的最大与和"""


class Solution:
    def maximumANDSum(self, nums: list[int], numSlots: int) -> int:
        capacity = 2 * numSlots
        memo = {0: 0}
        for value in nums:
            next_memo = {}
            for mask, score in memo.items():
                for slot in range(numSlots):
                    bit = 1 << (2 * slot)
                    if not mask & bit:
                        next_mask = mask | bit
                    elif not mask & (bit << 1):
                        next_mask = mask | (bit << 1)
                    else:
                        continue
                    next_memo[next_mask] = max(
                        next_memo.get(next_mask, 0), score + (value & (slot + 1))
                    )
            memo = next_memo
        return max(memo.values())


if __name__ == "__main__":
    assert Solution().maximumANDSum([1, 2, 3, 4, 5, 6], 3) == 9
