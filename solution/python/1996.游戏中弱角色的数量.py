"""1996. 游戏中弱角色的数量"""


class Solution:
    def numberOfWeakCharacters(self, properties: list[list[int]]) -> int:
        properties.sort(key=lambda item: (-item[0], item[1]))
        maximum_defense = 0
        result = 0
        for _, defense in properties:
            result += defense < maximum_defense
            maximum_defense = max(maximum_defense, defense)
        return result


if __name__ == "__main__":
    assert Solution().numberOfWeakCharacters([[5, 5], [6, 3], [3, 6]]) == 0
    assert Solution().numberOfWeakCharacters([[2, 2], [3, 3]]) == 1
