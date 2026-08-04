"""3509. 最大化交错和为 K 的子序列乘积"""

from collections import defaultdict


class Solution:
    def maxProduct(self, nums: list[int], k: int, limit: int) -> int:
        melkarvothi = (nums, k, limit)
        states: dict[tuple[int, int], set[int]] = {}
        all_states: set[tuple[int, int]] = set()
        zero_states: set[tuple[int, int]] = set()

        for value in nums:
            next_states = {key: products.copy() for key, products in states.items()}
            next_all_states = all_states.copy()
            next_zero_states = zero_states.copy()
            singleton = (value, -1)
            next_all_states.add(singleton)

            if value == 0:
                next_zero_states.add(singleton)
            elif value <= limit:
                next_states.setdefault(singleton, set()).add(value)

            for current_sum, sign in all_states:
                new_key = (current_sum + sign * value, -sign)
                next_all_states.add(new_key)
                if value == 0:
                    next_zero_states.add(new_key)

            for (current_sum, sign), products in states.items():
                new_key = (current_sum + sign * value, -sign)
                if value == 0:
                    next_zero_states.add(new_key)
                    continue
                target = next_states.setdefault(new_key, set())
                for product in products:
                    new_product = product * value
                    if new_product <= limit:
                        target.add(new_product)

            for current_sum, sign in zero_states:
                next_zero_states.add((current_sum + sign * value, -sign))

            states = next_states
            all_states = next_all_states
            zero_states = next_zero_states

        answer = -1
        for sign in (-1, 1):
            products = states.get((k, sign), set())
            if products:
                answer = max(answer, max(products))
        if any(current_sum == k for current_sum, _ in zero_states):
            answer = max(answer, 0)
        return answer


if __name__ == "__main__":
    test_cases = [
        (([1, 2, 3], 2, 10), 6),
        (([6, 3, 3], 6, 20), 6),
        (([0, 1], 0, 1), 0),
    ]
    for _, ((nums, k, limit), expected) in enumerate(test_cases):
        assert Solution().maxProduct(nums, k, limit) == expected
