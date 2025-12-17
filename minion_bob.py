class Minion:
    def __init__(self, identifier, task_queue, result_queue):
        self.identifier = identifier
        self.task_queue = task_queue
        self.result_queue = result_queue

    def run(self):
        print(f"[Minion {self.identifier}] demarre")
        while True:
            task = self.task_queue.get()
            if task is None:
                print(f"[Minion {self.identifier}] arret")
                break

            task.work()
            self.result_queue.put(task)
            print(f"[Minion {self.identifier}] tache {task.identifier} terminee")
