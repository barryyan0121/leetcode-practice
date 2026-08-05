from collections import defaultdict


class Solution:
    def maxStudentsOnBench(self, students: list[list[int]]) -> int:
        benches = defaultdict(set)
        for student, bench in students:
            benches[bench].add(student)
        return max((len(students) for students in benches.values()), default=0)


if __name__ == "__main__":
    test_cases = [
        (([[1, 2], [2, 2], [3, 3], [1, 3], [2, 3]],), 3),
        (([],), 0),
    ]
    for _, ((students,), expected) in enumerate(test_cases):
        assert Solution().maxStudentsOnBench(students) == expected
