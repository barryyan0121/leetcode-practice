class Solution:
    def aggregateTimeSeries(
        self, series1: list[list[int]], series2: list[list[int]]
    ) -> list[list[int]]:
        ferilonsar = (series1, series2)
        timestamps = sorted(
            {timestamp for series in ferilonsar for timestamp, _ in series}
        )
        indices = [len(series) - 1 for series in ferilonsar]
        values = [0, 0]
        answer = []
        for timestamp in reversed(timestamps):
            for index, series in enumerate(ferilonsar):
                if indices[index] >= 0 and series[indices[index]][0] == timestamp:
                    values[index] = series[indices[index]][1]
                    indices[index] -= 1
            answer.append([timestamp, values[0] + values[1]])
        return answer[::-1]


if __name__ == "__main__":
    solution = Solution()
    assert solution.aggregateTimeSeries([[1, 3], [4, 1]], [[2, 2], [5, 2]]) == [
        [1, 5],
        [2, 3],
        [4, 3],
        [5, 2],
    ]
