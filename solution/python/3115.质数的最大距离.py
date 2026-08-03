class Solution:
    def maximumPrimeDifference(self, nums: list[int]) -> int:
        limit = max(nums)
        prime = [True] * (limit + 1)
        if limit >= 0:
            prime[0] = False
        if limit >= 1:
            prime[1] = False
        for number in range(2, int(limit**0.5) + 1):
            if prime[number]:
                prime[number * number : limit + 1 : number] = [False] * (
                    ((limit - number * number) // number) + 1
                )

        first = next(index for index, value in enumerate(nums) if prime[value])
        last = next(
            index for index in range(len(nums) - 1, -1, -1) if prime[nums[index]]
        )
        return last - first


if __name__ == "__main__":
    test_cases = [([4, 2, 9, 5, 3], 3), ([4, 3, 4], 0)]
    for _, (nums, expected) in enumerate(test_cases):
        assert Solution().maximumPrimeDifference(nums) == expected
