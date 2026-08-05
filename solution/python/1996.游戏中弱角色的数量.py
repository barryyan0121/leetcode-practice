"""1996. 游戏中弱角色的数量"""


class Solution:
    def numberOfWeakCharacters(self, properties: list[list[int]]) -> int:
        properties.sort(key=lambda item: (-item[0], item[1]))
        strongest = answer = 0
        for _, defense in properties:
            if defense < strongest:
                answer += 1
            strongest = max(strongest, defense)
        return answer


if __name__ == "__main__":
    test_cases = [(([[5, 5], [6, 3], [3, 6]],), 0)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().numberOfWeakCharacters(*args) == expected
