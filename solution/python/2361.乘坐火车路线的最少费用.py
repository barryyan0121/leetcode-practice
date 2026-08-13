"""2361. 乘坐火车路线的最少费用"""


class Solution:
    def minimumCosts(
        self, regular: list[int], express: list[int], expressCost: int
    ) -> list[int]:
        normal, fast = 0, expressCost
        answer = []
        for regular_cost, express_cost in zip(regular, express):
            old_normal, old_fast = normal, fast
            normal = min(old_normal + regular_cost, old_fast + regular_cost)
            fast = min(old_fast + express_cost, old_normal + expressCost + express_cost)
            answer.append(min(normal, fast))
        return answer


if __name__ == "__main__":
    assert Solution().minimumCosts([1, 6, 9, 5], [5, 2, 3, 10], 8) == [1, 7, 14, 19]
