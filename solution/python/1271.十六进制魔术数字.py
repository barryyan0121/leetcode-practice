class Solution:
    def toHexspeak(self, num: str) -> str:
        result = hex(int(num))[2:].upper().replace("0", "O").replace("1", "I")
        return result if all(char in "ABCDEFIO" for char in result) else "ERROR"


if __name__ == "__main__":
    test_cases = [("257", "IOI"), ("3", "ERROR")]
    for _, (num, expected) in enumerate(test_cases):
        assert Solution().toHexspeak(num) == expected
