class Solution:
    def maximumLength(self, nums: list[int], k: int) -> int:
        ending = [{} for _ in range(k + 1)]
        best = [0] * (k + 1)
        best_value = [None] * (k + 1)
        second = [0] * (k + 1)

        for number in nums:
            for changes in range(k, -1, -1):
                length = ending[changes].get(number, 0) + 1
                if changes:
                    previous = (
                        best_value[changes - 1] != number
                        and best[changes - 1]
                        or second[changes - 1]
                    )
                    length = max(length, previous + 1)
                ending[changes][number] = length
                if best_value[changes] == number:
                    best[changes] = max(best[changes], length)
                elif length > best[changes]:
                    second[changes] = best[changes]
                    best[changes] = length
                    best_value[changes] = number
                else:
                    second[changes] = max(second[changes], length)
        return best[k]


if __name__ == "__main__":
    test_cases = [(([1, 2, 1, 1, 3], 2), 4), (([1, 2, 3, 4, 5, 1], 0), 2)]
    for _, ((nums, k), expected) in enumerate(test_cases):
        assert Solution().maximumLength(nums, k) == expected
