class Solution:
    def divisibleTripletCount(self, nums: list[int], d: int) -> int:
        answer = 0
        pairs = {}
        for right in range(2, len(nums)):
            middle = right - 1
            for left in range(middle):
                remainder = (nums[left] + nums[middle]) % d
                pairs[remainder] = pairs.get(remainder, 0) + 1
            answer += pairs.get((-nums[right]) % d, 0)
        return answer


if __name__ == "__main__":
    solution = Solution()
    assert solution.divisibleTripletCount([3, 3, 4, 7, 8], 5) == 3
    assert solution.divisibleTripletCount([3, 3, 3, 3], 3) == 4
    assert solution.divisibleTripletCount([3, 3, 3, 3], 6) == 0
