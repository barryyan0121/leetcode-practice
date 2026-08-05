"""1980. 找出不同的二进制字符串"""


class Solution:
    def findDifferentBinaryString(self, nums: list[str]) -> str:
        return "".join("1" if value[i] == "0" else "0" for i, value in enumerate(nums))


if __name__ == "__main__":
    test_cases = [((["01", "10"],), None)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().findDifferentBinaryString(*args) not in args[0]
