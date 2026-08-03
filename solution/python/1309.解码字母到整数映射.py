class Solution:
    def freqAlphabets(self, s: str) -> str:
        result, index = [], len(s) - 1
        while index >= 0:
            if s[index] == "#":
                result.append(chr(int(s[index - 2 : index]) + 96))
                index -= 3
            else:
                result.append(chr(int(s[index]) + 96))
                index -= 1
        return "".join(reversed(result))


if __name__ == "__main__":
    test_cases = [
        (Solution().freqAlphabets, ("10#11#12",), "jkab"),
        (Solution().freqAlphabets, ("1326#",), "acz"),
    ]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1309 题 "解码字母到整数映射" 所有测试用例通过')
