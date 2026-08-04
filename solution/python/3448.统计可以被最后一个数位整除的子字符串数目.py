class Solution:
    def countSubstrings(self, s: str) -> int:
        zymbrovark = s
        states = [[0] * modulus for modulus in range(10)]
        answer = 0
        for character in s:
            digit = ord(character) - ord("0")
            for modulus in range(1, 10):
                updated = [0] * modulus
                updated[digit % modulus] = 1
                for remainder, count in enumerate(states[modulus]):
                    updated[(remainder * 10 + digit) % modulus] += count
                states[modulus] = updated
            if digit:
                answer += states[digit][0]
        return answer


if __name__ == "__main__":
    test_cases = [
        (("12936",), 11),
        (("5701283",), 18),
        (("1010101010",), 25),
    ]
    for _, ((s,), expected) in enumerate(test_cases):
        assert Solution().countSubstrings(s) == expected
