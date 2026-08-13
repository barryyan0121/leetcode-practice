"""2222. 选择建筑的方案数"""


class Solution:
    def numberOfWays(self, s: str) -> int:
        zeros = s.count("0")
        ones = len(s) - zeros
        left_zero = left_one = answer = 0
        for char in s:
            if char == "0":
                answer += left_one * (ones - left_one)
                left_zero += 1
            else:
                answer += left_zero * (zeros - left_zero)
                left_one += 1
        return answer

if __name__ == "__main__":
    assert Solution().numberOfWays("001101") == 6
