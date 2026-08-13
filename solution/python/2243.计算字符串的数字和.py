"""2243. 计算字符串的数字和"""


class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            s = "".join(str(sum(map(int, s[i : i + k]))) for i in range(0, len(s), k))
        return s

if __name__ == "__main__":
    assert Solution().digitSum("11111222223", 3) == "135"
