from task import Task


class Boss:
    def __init__(self, task_queue, n_tasks):
        self.task_queue = task_queue
        self.n_tasks = n_tasks

    def run(self):
        print("[Boss] Creation des taches")
        for i in range(self.n_tasks):
            task = Task(identifier=i)
            self.task_queue.put(task)

        for _ in range(self.n_tasks):
            self.task_queue.put(None)

        print("[Boss] Toutes les taches envoyees")
