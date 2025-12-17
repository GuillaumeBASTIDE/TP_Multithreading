from manager import Manager, HOST, PORT, AUTHKEY
import os


def main():
    manager = Manager(address=(HOST, PORT), authkey=AUTHKEY)
    manager.connect()

    task_q = manager.get_task_queue()
    result_q = manager.get_result_queue()

    minion_id = os.getpid()
    print(f"[Minion {minion_id}] Démarré")

    while True:
        task = task_q.get()

        if task is None:
            print(f"[Minion {minion_id}] Signal d'arrêt reçu")
            break

        task.work()
        result_q.put(task)


if __name__ == "__main__":
    main()
