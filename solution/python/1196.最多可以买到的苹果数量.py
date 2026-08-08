#
# @lc app=leetcode.cn id=1196 lang=python3
#
# [1196] 最多可以买到的苹果数量
#


# @lc code=start
class Solution:
    def maxNumberOfApples(self, weight):
        total = count = 0
        for value in sorted(weight):
            if total + value > 5000:
                break
            total += value
            count += 1
        return count


# @lc code=end


if __name__ == "__main__":
    test_cases = [
        (([100, 200, 150, 1000],), 4),
        (([900, 950, 800, 1000, 700, 800],), 5),
    ]
    for index, (args, expected) in enumerate(test_cases):
        assert Solution().maxNumberOfApples(*args) == expected, index
