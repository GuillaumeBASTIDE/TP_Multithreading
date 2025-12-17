import time
import json
import numpy as np


class Task:
    def __init__(self, identifier: str, size: int):
        self.identifier = identifier
        self.size = size
        self.time = None
        self.a = None
        self.b = None

    def work(self):
        start = time.perf_counter()
        self.x = np.linalg.solve(self.a, self.b)
        self.time = time.perf_counter() - start

    def to_json(self) -> str:
        data = {
            "identifier": self.identifier,
            "size": self.size,
            "time": self.time,
            "a": self.a.tolist() if self.a is not None else None,
            "b": self.b.tolist() if self.b is not None else None,
        }
        return json.dumps(data, indent=2)

    @staticmethod
    def from_json(text: str) -> "Task":
        data = json.loads(text)
        task = Task(identifier=data["identifier"], size=data["size"])
        task.time = data["time"]
        task.a = np.array(data["a"]) if data["a"] is not None else None
        task.b = np.array(data["b"]) if data["b"] is not None else None
        return task

    def __eq__(self, other) -> bool:
        if not isinstance(other, Task):
            return False

        if (
            self.identifier != other.identifier
            or self.size != other.size
            or self.time != other.time
        ):
            return False

        tolerance = 1e-10
        if not np.allclose(self.a, other.a, rtol=tolerance, atol=tolerance):
            return False
        if not np.allclose(self.b, other.b, rtol=tolerance, atol=tolerance):
            return False
        if not np.allclose(self.x, other.x, rtol=tolerance, atol=tolerance):
            return False

        return True
