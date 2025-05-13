#
# @lc app=leetcode.cn id=2094 lang=python3
# @lcpr version=30201
#
# [2094] 找出 3 位偶数
#


# @lc code=start
class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        res = []  # 目标偶数数组
        freq = Counter(digits)  # 整数数组中各数字的出现次数
        # 枚举所有三位偶数，维护整数中各数位的出现次数并比较判断是否为目标偶数
        for i in range(100, 1000, 2):
            freq1 = Counter([int(d) for d in str(i)])
            if all(freq[d] >= freq1[d] for d in freq1.keys()):
                res.append(i)
        return res


# @lc code=end


#
# @lcpr case=start
# [2,1,3,0]\n
# @lcpr case=end

# @lcpr case=start
# [2,2,8,8,2]\n
# @lcpr case=end

# @lcpr case=start
# [3,7,5]\n
# @lcpr case=end

#
