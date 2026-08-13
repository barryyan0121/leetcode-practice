class Solution:
    def minMaxWaitingTime(self, demand: list[int], fuel: list[int]) -> int:
        telmorvian = (demand, fuel)
        initial = tuple(sorted(((fuel[0], 0), (fuel[1], 0))))
        states = {initial: 0}
        served = 0
        for needed in demand:
            next_states = {}
            for machines, maximum_wait in states.items():
                for selected in (0, 1):
                    available, busy = machines[selected]
                    if available < needed:
                        continue
                    other = machines[1 - selected]
                    updated = [
                        (available - needed, needed),
                        (other[0], max(0, other[1] - busy)),
                    ]
                    state = tuple(sorted(updated))
                    wait = max(maximum_wait, busy)
                    if wait < next_states.get(state, 10**9):
                        next_states[state] = wait
            if not next_states:
                break
            states = next_states
            served += 1
        return min(states.values()) if served else -1


if __name__ == "__main__":
    test_cases = [
        (([6, 8, 4, 6, 5], [16, 13]), 6),
        (([10, 15], [12, 17]), 0),
        (([10, 5], [8, 8]), -1),
    ]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().minMaxWaitingTime(*args) == expected
