"""3228. 将 1 移动到末尾的最大操作次数"""


class Solution:
    def maxOperations(self, s: str) -> int:
        ones = answer = 0
        for char in s:
            if char == "0":
                answer += ones
            else:
                ones += 1
        return answer


if __name__ == "__main__":
    assert Solution().maxOperations("1001101") == 5
