from multiprocessing.managers import BaseManager
from multiprocessing import Queue

HOST = "localhost"
PORT = 50000

class Manager(BaseManager):
    pass

task_queue = Queue()
result_queue = Queue()

Manager.register("get_task_queue", callable=lambda: task_queue)
Manager.register("get_result_queue", callable=lambda: result_queue)

def main():
    manager = Manager(address=(HOST, PORT), authkey=AUTHKEY)
    server = manager.get_server()
    print("[Manager] Serveur démarré")
    server.serve_forever()

if __name__ == "__main__":
    main()
