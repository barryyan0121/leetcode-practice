"""2433. 找出前缀异或的原始数组"""


class Solution:
    def findArray(self, pref: list[int]) -> list[int]:
        answer = [pref[0]]
        for previous, current in zip(pref, pref[1:]):
            answer.append(previous ^ current)
        return answer


if __name__ == "__main__":
    test_cases = [(([5, 2, 0, 3, 1],), [5, 7, 2, 3, 2])]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().findArray(*args) == expected
