from typing import List


class Solution:
    def alternatingXOR(self, nums: List[int], target1: int, target2: int) -> int:
        mod = 10**9 + 7
        states = {0: (1, 0)}  # next segment must match target1 / target2
        prefix = 0
        answer = 0
        for value in nums:
            prefix ^= value
            a = states.get(prefix ^ target1, (0, 0))
            b = states.get(prefix ^ target2, (0, 0))
            next_state = (b[1] % mod, a[0] % mod)
            states[prefix] = tuple(
                (states.get(prefix, (0, 0))[i] + next_state[i]) % mod for i in range(2)
            )
            answer = sum(next_state) % mod
        return answer


if __name__ == "__main__":
    s = Solution()
    assert s.alternatingXOR([2, 3, 1, 4], 1, 5) == 1
    assert s.alternatingXOR([1, 0, 0], 1, 0) == 3
    assert s.alternatingXOR([7], 1, 7) == 0
