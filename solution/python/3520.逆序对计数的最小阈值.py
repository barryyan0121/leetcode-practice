from bisect import bisect_right


class Solution:
    def minThreshold(self, nums: list[int], k: int) -> int:
        ordered = sorted(nums)
        size = len(ordered)

        def count(threshold: int) -> int:
            bit = [0] * (size + 1)

            def add(index: int) -> None:
                index += 1
                while index <= size:
                    bit[index] += 1
                    index += index & -index

            def prefix(end: int) -> int:
                answer = 0
                while end:
                    answer += bit[end]
                    end -= end & -end
                return answer

            answer = 0
            for value in nums:
                left = bisect_right(ordered, value)
                right = bisect_right(ordered, value + threshold)
                answer += prefix(right) - prefix(left)
                if answer >= k:
                    return answer
                add(bisect_right(ordered, value) - 1)
            return answer

        if count(max(nums) - min(nums)) < k:
            return -1
        low, high = 0, max(nums) - min(nums)
        while low < high:
            middle = (low + high) // 2
            if count(middle) >= k:
                high = middle
            else:
                low = middle + 1
        return low


if __name__ == "__main__":
    test_cases = [(([1, 2, 3, 4, 3, 2, 1], 7), 2), (([10, 9, 9, 9, 1], 4), 8)]
    for _, ((nums, k), expected) in enumerate(test_cases):
        assert Solution().minThreshold(nums, k) == expected
