from functools import cmp_to_key


class Solution:
    def minDamage(self, power: int, damage: list[int], health: list[int]) -> int:
        enemies = [
            ((value + power - 1) // power, hit) for value, hit in zip(health, damage)
        ]

        def compare(left: tuple[int, int], right: tuple[int, int]) -> int:
            left_time, left_damage = left
            right_time, right_damage = right
            return left_time * right_damage - right_time * left_damage

        enemies.sort(key=cmp_to_key(compare))
        active_damage = sum(damage)
        answer = 0
        for time, hit_damage in enemies:
            answer += active_damage * time
            active_damage -= hit_damage
        return answer


if __name__ == "__main__":
    test_cases = [
        ((4, [1, 2, 3, 4], [4, 5, 6, 8]), 39),
        ((1, [1, 1, 1, 1], [1, 2, 3, 4]), 20),
        ((8, [40], [59]), 320),
    ]
    for _, ((power, damage, health), expected) in enumerate(test_cases):
        assert Solution().minDamage(power, damage, health) == expected
