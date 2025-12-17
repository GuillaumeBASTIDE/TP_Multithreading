import multiprocessing as mp
from boss_gru import Boss
from minion_bob import Minion


class QueueManager:
    def __init__(self, n_minions=2):
        self.task_queue = mp.Queue()
        self.result_queue = mp.Queue()
        self.n_minions = n_minions
        self.processes = []

    def start(self, n_tasks=5):
        boss = Boss(self.task_queue, n_tasks)
        boss_process = mp.Process(target=boss.run)
        self.processes.append(boss_process)
        boss_process.start()

        for i in range(self.n_minions):
            minion = Minion(i, self.task_queue, self.result_queue)
            p = mp.Process(target=minion.run)
            self.processes.append(p)
            p.start()

    def stop(self):
        for p in self.processes:
            p.join()
