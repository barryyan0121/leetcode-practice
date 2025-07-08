#
# @lc app=leetcode.cn id=1931 lang=python3
# @lcpr version=30201
#
# [1931] 用三种不同颜色为网格涂色
#

# @lc code=start
class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        mod = 10**9 + 7
        # 哈希映射 valid 存储所有满足要求的对一行进行涂色的方案
        # 键表示 mask，值表示 mask 的三进制串（以列表的形式存储）
        valid = dict()

        # 在 [0, 3^m) 范围内枚举满足要求的 mask
        for mask in range(3**m):
            color = list()
            mm = mask
            for i in range(m):
                color.append(mm % 3)
                mm //= 3
            if any(color[i] == color[i + 1] for i in range(m - 1)):
                continue
            valid[mask] = color

        # 预处理所有的 (mask1, mask2) 二元组，满足 mask1 和 mask2 作为相邻行时，同一列上两个格子的颜色不同
        adjacent = defaultdict(list)
        for mask1, color1 in valid.items():
            for mask2, color2 in valid.items():
                if not any(x == y for x, y in zip(color1, color2)):
                    adjacent[mask1].append(mask2)

        f = [int(mask in valid) for mask in range(3**m)]
        for i in range(1, n):
            g = [0] * (3**m)
            for mask2 in valid.keys():
                for mask1 in adjacent[mask2]:
                    g[mask2] += f[mask1]
                    if g[mask2] >= mod:
                        g[mask2] -= mod
            f = g

        return sum(f) % mod

# @lc code=end



#
# @lcpr case=start
# 1\n1\n
# @lcpr case=end

# @lcpr case=start
# 1\n2\n
# @lcpr case=end

# @lcpr case=start
# 5\n5\n
# @lcpr case=end

#

