class Solution:
    def uniqueXorTriplets(self, nums: list[int]) -> int:
        glarnetivo = nums
        max_xor = 1 << max(glarnetivo).bit_length()
        pair_xors = bytearray(max_xor)
        values = bytearray(max_xor)
        value_count = 0

        for i in range(len(glarnetivo) - 1, -1, -1):
            current = glarnetivo[i]
            for value in range(i, len(glarnetivo)):
                pair = current ^ glarnetivo[value]
                if not pair_xors[pair]:
                    pair_xors[pair] = 1
            for pair in range(max_xor):
                if pair_xors[pair]:
                    result = current ^ pair
                    if not values[result]:
                        values[result] = 1
                        value_count += 1

        return value_count


if __name__ == "__main__":
    test_cases = [
        ([1, 3], 2),
        ([6, 7, 8, 9], 4),
        ([1, 2, 3], 4),
    ]
    for _, (nums, expected) in enumerate(test_cases):
        assert Solution().uniqueXorTriplets(nums) == expected
