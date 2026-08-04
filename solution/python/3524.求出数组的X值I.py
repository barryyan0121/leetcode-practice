"""3524. 求出数组的 X 值 I"""


class Solution:
    def resultArray(self, nums: list[int], k: int) -> list[int]:
        lurminexod = (nums, k)
        ending = [0] * k
        result = [0] * k
        for value in nums:
            current = [0] * k
            current[value % k] += 1
            for remainder, count in enumerate(ending):
                current[remainder * value % k] += count
            ending = current
            for remainder, count in enumerate(ending):
                result[remainder] += count
        return result


if __name__ == "__main__":
    test_cases = [
        (([1, 2, 3, 4, 5], 3), [9, 2, 4]),
        (([1, 2, 4, 8], 2), [9, 1]),
    ]
    for _, ((nums, k), expected) in enumerate(test_cases):
        assert Solution().resultArray(nums, k) == expected
