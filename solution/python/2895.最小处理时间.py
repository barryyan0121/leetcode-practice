"""2895. 最小处理时间"""


class Solution:
    def minProcessingTime(self, processorTime: list[int], tasks: list[int]) -> int:
        processorTime.sort()
        tasks.sort(reverse=True)
        return max(
            processor + tasks[index * 4]
            for index, processor in enumerate(processorTime)
        )


if __name__ == "__main__":
    assert Solution().minProcessingTime([8, 10], [2, 2, 3, 1, 8, 7, 4, 5]) == 16
