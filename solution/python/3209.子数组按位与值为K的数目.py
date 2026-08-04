class Solution:
    def countSubarrays(self, nums: list[int], k: int) -> int:
        previous = []
        answer = 0
        for number in nums:
            current = [(number, 1)]
            for value, count in previous:
                merged = value & number
                if current[-1][0] == merged:
                    current[-1] = (merged, current[-1][1] + count)
                else:
                    current.append((merged, count))
            answer += sum(count for value, count in current if value == k)
            previous = current
        return answer


if __name__ == "__main__":
    test_cases = [(([1, 1, 1], 1), 6), (([1, 1, 2], 1), 3), (([1, 2, 3], 2), 2)]
    for _, ((nums, k), expected) in enumerate(test_cases):
        assert Solution().countSubarrays(nums, k) == expected
