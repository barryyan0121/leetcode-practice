class Solution:
    def countOfPeaks(self, nums: list[int], queries: list[list[int]]) -> list[int]:
        n = len(nums)
        tree = [0] * (n + 1)
        peaks = [False] * n

        def is_peak(index: int) -> bool:
            return (
                0 < index < n - 1
                and nums[index] > nums[index - 1]
                and nums[index] > nums[index + 1]
            )

        def add(index: int, delta: int) -> None:
            index += 1
            while index <= n:
                tree[index] += delta
                index += index & -index

        def prefix(index: int) -> int:
            total = 0
            while index:
                total += tree[index]
                index -= index & -index
            return total

        for index in range(n):
            peaks[index] = is_peak(index)
            if peaks[index]:
                add(index, 1)

        answer = []
        for query_type, left, right in queries:
            if query_type == 1:
                answer.append(
                    prefix(right) - prefix(left + 1) if left + 1 < right else 0
                )
            else:
                nums[left] = right
                for index in range(max(0, left - 1), min(n, left + 2)):
                    current = is_peak(index)
                    if current != peaks[index]:
                        add(index, 1 if current else -1)
                        peaks[index] = current
        return answer


if __name__ == "__main__":
    test_cases = [
        (([3, 1, 4, 2, 5], [[2, 3, 4], [1, 0, 4]]), [0]),
        (([4, 1, 4, 2, 1, 5], [[2, 2, 4], [1, 0, 2], [1, 0, 4]]), [0, 1]),
        (([5, 4, 8, 6], [[1, 2, 2], [1, 1, 2], [2, 1, 6]]), [0, 0]),
    ]
    for _, ((nums, queries), expected) in enumerate(test_cases):
        assert Solution().countOfPeaks(nums, queries) == expected
