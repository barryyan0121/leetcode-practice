class Solution:
    def lastStoneWeightII(self, stones: list[int]) -> int:
        total = sum(stones)
        bits = 1
        for stone in stones:
            bits |= bits << stone
        best = (bits & ((1 << (total // 2 + 1)) - 1)).bit_length() - 1
        return total - 2 * best


if __name__ == "__main__":
    test_cases = [
        ([2, 7, 4, 1, 8, 1], 1),
        ([31, 26, 33, 21, 40], 5),
        ([1, 1, 4, 2, 2], 0),
    ]
    for _, (stones, expected) in enumerate(test_cases):
        assert Solution().lastStoneWeightII(stones) == expected
