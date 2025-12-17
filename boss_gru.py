from manager import Manager, HOST, PORT, AUTHKEY
from task import Task
import time

NUM_TASKS = 6
NUM_MINIONS = 2

def main():
    manager = Manager(address=(HOST, PORT), authkey=AUTHKEY)
    manager.connect()

    task_q = manager.get_task_queue()
    result_q = manager.get_result_queue()

    print("[Boss] Envoi des tâches")
    for i in range(NUM_TASKS):
        task_q.put(Task(identifier=i, size=200))

    start = time.perf_counter()

    for _ in range(NUM_TASKS):
        result = result_q.get()
        print(f"[Boss] Résultat tâche {result.identifier} en {result.time:.4f}s")

    print(f"[Boss] Temps total : {time.perf_counter() - start:.2f}s")

    for _ in range(NUM_MINIONS):
        task_q.put(None)

if __name__ == "__main__":
    main()
