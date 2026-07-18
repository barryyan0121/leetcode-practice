from threading import Barrier, Semaphore, Thread


class H2O:
    def __init__(self):
        self.hydrogen_turn = Semaphore(2)
        self.oxygen_turn = Semaphore(1)
        self.barrier = Barrier(3, self.reset)

    def reset(self) -> None:
        self.hydrogen_turn.release()
        self.hydrogen_turn.release()
        self.oxygen_turn.release()

    def hydrogen(self, releaseHydrogen) -> None:
        self.hydrogen_turn.acquire()
        releaseHydrogen()
        self.barrier.wait()

    def oxygen(self, releaseOxygen) -> None:
        self.oxygen_turn.acquire()
        releaseOxygen()
        self.barrier.wait()


if __name__ == "__main__":
    test_cases = [1, 3]
    for _, count in enumerate(test_cases):
        output = []
        h2o = H2O()
        threads = [
            Thread(target=h2o.oxygen, args=(lambda: output.append("O"),))
            for _ in range(count)
        ] + [
            Thread(target=h2o.hydrogen, args=(lambda: output.append("H"),))
            for _ in range(count * 2)
        ]
        for thread in threads:
            thread.start()
        for thread in threads:
            thread.join()
        assert len(output) == count * 3
        assert all(
            sorted(output[index : index + 3]) == ["H", "H", "O"]
            for index in range(0, len(output), 3)
        )
