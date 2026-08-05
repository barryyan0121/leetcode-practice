"""2143. 在两个数组的区间中选取数字"""


class Solution:
    def countSubranges(self, nums1: list[int], nums2: list[int]) -> int:
        modulo = 10**9 + 7
        states = {}
        answer = 0
        for first, second in zip(nums1, nums2):
            next_states = {first: 1}
            next_states[-second] = next_states.get(-second, 0) + 1
            for total, count in states.items():
                next_states[total + first] = (
                    next_states.get(total + first, 0) + count
                ) % modulo
                next_states[total - second] = (
                    next_states.get(total - second, 0) + count
                ) % modulo
            answer = (answer + next_states.get(0, 0)) % modulo
            states = next_states
        return answer


if __name__ == "__main__":
    test_cases = [(([1, 2, 5], [2, 6, 3]), 3), (([0, 1], [1, 0]), 4)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().countSubranges(*args) == expected
