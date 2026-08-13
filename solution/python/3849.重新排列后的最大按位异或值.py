"""3849. 重新排列后的最大按位异或值"""


class Solution:
    def maximumXor(self, s: str, t: str) -> str:
        zeros = t.count("0")
        ones = len(t) - zeros
        answer: list[str] = []
        for ch in s:
            if ch == "0":
                if ones:
                    answer.append("1")
                    ones -= 1
                else:
                    answer.append("0")
                    zeros -= 1
            else:
                if zeros:
                    answer.append("1")
                    zeros -= 1
                else:
                    answer.append("0")
                    ones -= 1
        return "".join(answer)


if __name__ == "__main__":
    test_cases = [(("101", "011"), "110"), (("0110", "1110"), "1101"), (("0101", "1001"), "1111")]
    for args, expected in test_cases:
        assert Solution().maximumXor(*args) == expected
