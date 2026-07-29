from threading import Lock, Semaphore


class DiningPhilosophers:
    def __init__(self):
        self.forks = [Lock() for _ in range(5)]
        self.table = Semaphore(4)

    def wantsToEat(
        self, philosopher, pickLeftFork, pickRightFork, eat, putLeftFork, putRightFork
    ):
        left, right = philosopher, (philosopher + 1) % 5
        with self.table, self.forks[left], self.forks[right]:
            pickLeftFork()
            pickRightFork()
            eat()
            putLeftFork()
            putRightFork()


if __name__ == "__main__":
    test_cases = [0]
    for _, philosopher in enumerate(test_cases):
        actions = []
        DiningPhilosophers().wantsToEat(
            philosopher, *(lambda x=x: actions.append(x) for x in range(5))
        )
        assert actions == [0, 1, 2, 3, 4]
