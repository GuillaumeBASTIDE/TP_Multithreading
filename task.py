import time
import numpy as np
import json
from dataclasses import dataclass, field
from typing import Dict, Any

class Task:
    def __init__(self, identifier=0, size=None):
        self.identifier = identifier
        # choosee the size of the problem
        self.size = size or np.random.randint(300, 3_000)
        # Generate the input of the problem
        self.a = np.random.rand(self.size, self.size)
        self.b = np.random.rand(self.size)
        # prepare room for the results
        self.x = np.zeros((self.size))
        self.time = 0

    def work(self):
        start = time.perf_counter()
        self.x = np.linalg.solve(self.a, self.b)
        self.time = time.perf_counter() - start

	# Ajout des méthodes

	def to_json(self) -> str :
		data = {
			"identifier": self.identifier,
			"size": self.size,
			"a": self.a.tolist(),
            "b": self.b.tolist(),
            "x": self.x.tolist(),
            "time": self.time
        }
        return json.dumps(data, indent=2)

	@staticmethod
	def from_json(text: str) -> "Task":
		data = json.loads(text)
        task = Task(identifier=data["identifier"], size=data["size"])
        task.a = np.array(data["a"])
        task.b = np.array(data["b"])
        task.x = np.array(data["x"])
        task.time = data["time"]
        return task

	def __eq__(self, other: "Task") -> bool:
		if not isinstance(other, Task):
            return False
        if (self.identifier != other.identifier or
            self.size != other.size or
            self.time != other.time):
            return False
        tolerance = 1e-10
        if not np.allclose(self.a, other.a, rtol=tolerance, atol=tolerance):
            return False
        if not np.allclose(self.b, other.b, rtol=tolerance, atol=tolerance):
            return False
        if not np.allclose(self.x, other.x, rtol=tolerance, atol=tolerance):
            return False
        return True
