from array import array


class Solution:
    def maximumSubarrayXor(
        self, nums: list[int], queries: list[list[int]]
    ) -> list[int]:
        n = len(nums)
        stride = n
        scores = array("I", [0]) * (n * n)
        best = array("I", [0]) * (n * n)
        for index, value in enumerate(nums):
            scores[index * stride + index] = value
            best[index * stride + index] = value

        for length in range(2, n + 1):
            for left in range(n - length + 1):
                right = left + length - 1
                position = left * stride + right
                scores[position] = (
                    scores[left * stride + right - 1]
                    ^ scores[(left + 1) * stride + right]
                )
                best[position] = max(
                    scores[position],
                    best[left * stride + right - 1],
                    best[(left + 1) * stride + right],
                )
        return [best[left * stride + right] for left, right in queries]


if __name__ == "__main__":
    test_cases = [
        (([2, 8, 4, 32, 16, 1], [[0, 2], [1, 4], [0, 5]]), [12, 60, 60]),
        (
            ([0, 7, 3, 2, 8, 5, 1], [[0, 3], [1, 5], [2, 4], [2, 6], [5, 6]]),
            [7, 14, 11, 14, 5],
        ),
    ]
    for _, ((nums, queries), expected) in enumerate(test_cases):
        assert Solution().maximumSubarrayXor(nums, queries) == expected
