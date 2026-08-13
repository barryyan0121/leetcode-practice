"""2289. 使数组按非递减顺序排列"""


class Solution:
    def totalSteps(self, nums: list[int]) -> int:
        stack = []
        answer = 0
        for value in nums:
            days = 0
            while stack and stack[-1][0] <= value:
                days = max(days, stack.pop()[1])
            if stack:
                days += 1
                answer = max(answer, days)
            else:
                days = 0
            stack.append((value, days))
        return answer

if __name__ == "__main__":
    assert Solution().totalSteps([5,3,4,4,7,3,6,11,8,5,11]) == 3
