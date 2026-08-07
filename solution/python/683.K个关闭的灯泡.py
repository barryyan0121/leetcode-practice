#
# @lc app=leetcode.cn id=683 lang=python3
#
# [683] K 个关闭的灯泡
#


# @lc code=start
class Solution:
    def kEmptySlots(self, bulbs, k: int) -> int:
        n = len(bulbs)
        days = [0] * n
        for day, position in enumerate(bulbs, 1):
            days[position - 1] = day
        answer = float("inf")
        left, right = 0, k + 1
        while right < n:
            valid = True
            for i in range(left + 1, right):
                if days[i] < max(days[left], days[right]):
                    left, right = i, i + k + 1
                    valid = False
                    break
            if valid:
                answer = min(answer, max(days[left], days[right]))
                left, right = right, right + k + 1
        return -1 if answer == float("inf") else answer


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    assert solution.kEmptySlots([1, 3, 2], 1) == 2
    assert solution.kEmptySlots([1, 2, 3], 1) == -1
