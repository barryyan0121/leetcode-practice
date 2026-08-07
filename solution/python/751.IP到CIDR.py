#
# @lc app=leetcode.cn id=751 lang=python3
#
# [751] IP 到 CIDR
#


# @lc code=start
class Solution:
    def ipToCIDR(self, ip: str, n: int):
        value = 0
        for part in ip.split("."):
            value = value * 256 + int(part)
        result = []
        while n:
            size = min(value & -value or 1 << 32, 1 << (n.bit_length() - 1))
            prefix = 32 - size.bit_length() + 1
            address = ".".join(str((value >> shift) & 255) for shift in (24, 16, 8, 0))
            result.append(f"{address}/{prefix}")
            value += size
            n -= size
        return result


# @lc code=end


if __name__ == "__main__":
    assert Solution().ipToCIDR("255.0.0.7", 10) == [
        "255.0.0.7/32",
        "255.0.0.8/29",
        "255.0.0.16/32",
    ]
