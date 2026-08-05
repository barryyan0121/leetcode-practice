class Solution:
    def makeArrayPositive(self, nums: list[int]) -> int:
        prefix = [0]
        for value in nums:
            prefix.append(prefix[-1] + value)

        chosen = -1
        answer = 0
        for right in range(2, len(nums)):
            for length in range(3, min(5, right + 1) + 1):
                left = right - length + 1
                if prefix[right + 1] - prefix[left] <= 0 and chosen < left:
                    chosen = right
                    answer += 1
                    break
        return answer


if __name__ == "__main__":
    test_cases = [
        (([-10, 15, -12],), 1),
        (([-1, -2, 3, -1, 2, 6],), 1),
        (([1, 2, 3],), 0),
    ]
    for _, ((nums,), expected) in enumerate(test_cases):
        assert Solution().makeArrayPositive(nums) == expected
