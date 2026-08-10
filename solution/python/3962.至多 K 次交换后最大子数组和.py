"""3962. 至多 K 次交换后最大子数组和"""


class Solution:
    def maxSum(self, nums: list[int], k: int) -> int:
        class Fenwick:
            def __init__(self, size: int):
                self.count = [0] * (size + 1)
                self.total = [0] * (size + 1)

            def add(self, index: int, count: int, value: int) -> None:
                while index < len(self.count):
                    self.count[index] += count
                    self.total[index] += count * value
                    index += index & -index

            def prefix(self, index: int) -> tuple[int, int]:
                count = total = 0
                while index:
                    count += self.count[index]
                    total += self.total[index]
                    index -= index & -index
                return count, total

            def kth_sum(self, amount: int, values: list[int]) -> int:
                if amount <= 0:
                    return 0
                position = 0
                count = total = 0
                step = 1 << (len(self.count).bit_length() - 1)
                while step:
                    candidate = position + step
                    if (
                        candidate < len(self.count)
                        and count + self.count[candidate] <= amount
                    ):
                        position = candidate
                        count += self.count[candidate]
                        total += self.total[candidate]
                    step >>= 1
                if count == amount:
                    return total
                return total + (amount - count) * values[position]

            def kth_complement(
                self,
                amount: int,
                full_count: list[int],
                full_total: list[int],
                values: list[int],
            ) -> int:
                if amount <= 0:
                    return 0
                position = 0
                count = total = 0
                step = 1 << (len(self.count).bit_length() - 1)
                while step:
                    candidate = position + step
                    if candidate < len(self.count):
                        candidate_count = full_count[candidate] - self.count[candidate]
                        if count + candidate_count <= amount:
                            position = candidate
                            count += candidate_count
                            total += full_total[candidate] - self.total[candidate]
                    step >>= 1
                if count == amount:
                    return total
                return total + (amount - count) * values[position]

        values = sorted(set(nums))
        ranks = {value: index + 1 for index, value in enumerate(values)}
        ordered = sorted(nums)
        size = len(values)
        all_count = [0] * (size + 1)
        all_total = [0] * (size + 1)
        raw_count = [0] * (size + 1)
        raw_total = [0] * (size + 1)
        for value in nums:
            rank = ranks[value]
            all_count[rank] += 1
            all_total[rank] += value
            raw_count[rank] += 1
            raw_total[rank] += value
        for rank in range(1, size + 1):
            parent = rank + (rank & -rank)
            if parent <= size:
                all_count[parent] += all_count[rank]
                all_total[parent] += all_total[rank]
        all_prefix_count = [0] * (size + 1)
        all_prefix_total = [0] * (size + 1)
        for rank in range(1, size + 1):
            all_prefix_count[rank] = all_prefix_count[rank - 1] + raw_count[rank]
            all_prefix_total[rank] = all_prefix_total[rank - 1] + raw_total[rank]
        total_sum = sum(nums)
        answer = -(10**30)
        for left in range(len(nums)):
            inside = Fenwick(size)
            inside_freq = [0] * (size + 1)
            inside_sum = 0
            base = 0
            for right in range(left, len(nums)):
                value = nums[right]
                rank = ranks[value]
                inside.add(rank, 1, value)
                inside_freq[rank] += 1
                inside_sum += value
                length = right - left + 1
                limit = min(k, length, len(nums) - length)
                base += value

                outside_count = len(nums) - length
                if outside_count == 0:
                    profitable = 0
                    best_gain = 0
                else:
                    threshold_rank = ranks[ordered[outside_count - 1]]
                    inside_through_threshold, inside_sum_through_threshold = (
                        inside.prefix(threshold_rank)
                    )
                    previous_inside = (
                        inside_through_threshold - inside_freq[threshold_rank]
                    )
                    outside_through_threshold = (
                        all_prefix_count[threshold_rank] - inside_through_threshold
                    )
                    profitable = max(
                        previous_inside,
                        min(
                            inside_through_threshold,
                            outside_count - outside_through_threshold,
                        ),
                    )
                    profitable = min(profitable, limit)
                    threshold_value = values[threshold_rank - 1]
                    if profitable < previous_inside:
                        smallest = inside.kth_sum(profitable, values)
                    else:
                        smallest = (
                            inside_sum_through_threshold
                            - inside_freq[threshold_rank] * threshold_value
                            + (profitable - previous_inside) * threshold_value
                        )
                    outside_sum = total_sum - inside_sum
                    outside_greater_sum = outside_sum - (
                        all_prefix_total[threshold_rank] - inside_sum_through_threshold
                    )
                    if profitable == outside_count - outside_through_threshold:
                        largest = outside_greater_sum
                    else:
                        largest = outside_sum - inside.kth_complement(
                            outside_count - profitable,
                            all_count,
                            all_total,
                            values,
                        )
                    best_gain = largest - smallest
                answer = max(answer, base + best_gain)
        return answer


if __name__ == "__main__":
    test_cases = [(([1, -1, 0, 2], 1), 3), (([4, 3, 2, 4], 2), 13), (([-1, -2], 0), -1)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().maxSum(*args) == expected
