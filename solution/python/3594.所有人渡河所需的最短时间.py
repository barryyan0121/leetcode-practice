"""3594. 所有人渡河所需的最短时间"""

import heapq


class Solution:
    def minTime(
        self, n: int, k: int, m: int, time: list[int], mul: list[float]
    ) -> float:
        romelytavn = time
        full = (1 << n) - 1
        group_max = [0] * (1 << n)
        group_size = [0] * (1 << n)
        for mask in range(1, 1 << n):
            bit = mask & -mask
            index = bit.bit_length() - 1
            rest = mask ^ bit
            group_size[mask] = group_size[rest] + 1
            group_max[mask] = max(group_max[rest], time[index])
        infinity = float("inf")
        distance = [infinity] * ((1 << n) * m)
        distance[0] = 0.0
        heap = [(0.0, 0, 0)]
        best = infinity
        while heap:
            current, mask, stage = heapq.heappop(heap)
            if current != distance[mask * m + stage] or current >= best:
                continue
            available = full ^ mask
            sub = available
            while sub:
                if group_size[sub] <= k:
                    duration = group_max[sub] * mul[stage]
                    next_stage = (stage + int(duration + 1e-9) % m) % m
                    moved = mask | sub
                    total = current + duration
                    if moved == full:
                        best = min(best, total)
                    else:
                        returned = moved
                        while returned:
                            bit = returned & -returned
                            person = bit.bit_length() - 1
                            return_time = time[person] * mul[next_stage]
                            final_stage = (next_stage + int(return_time + 1e-9) % m) % m
                            final_mask = moved ^ bit
                            final_distance = total + return_time
                            state = final_mask * m + final_stage
                            if final_distance < distance[state]:
                                distance[state] = final_distance
                                heapq.heappush(
                                    heap,
                                    (final_distance, final_mask, final_stage),
                                )
                            returned ^= bit
                sub = (sub - 1) & available
        return -1.0 if best == infinity else best


if __name__ == "__main__":
    test_cases = [
        ((1, 1, 2, [5], [1.0, 1.3]), 5.0),
        ((3, 2, 3, [2, 5, 8], [1.0, 1.5, 0.75]), 14.5),
        ((2, 1, 2, [10, 10], [2.0, 2.0]), -1.0),
    ]
    for _, ((n, k, m, time, mul), expected) in enumerate(test_cases):
        assert abs(Solution().minTime(n, k, m, time, mul) - expected) < 1e-9
