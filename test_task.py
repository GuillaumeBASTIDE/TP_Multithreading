import unittest
import json
import numpy as np
from numpy.testing import assert_allclose
from task import Task


class TestTask(unittest.TestCase):
    def test_task_work_solves_linear_system(self):
        size = 10
        task = Task(identifier=1, size=size)
        task.work()
        assert_allclose(task.a @ task.x, task.b, rtol=1e-7, atol=1e-9)
        self.assertGreaterEqual(task.time, 0.0)

    def test_json_serialization_roundtrip(self):
        original = Task(identifier=42, size=20)
        original.work()
        json_str = original.to_json()
        self.assertIsInstance(json_str, str)
        parsed = json.loads(json_str)
        self.assertEqual(parsed["identifier"], 42)
        self.assertEqual(parsed["size"], 20)
        restored = Task.from_json(json_str)
        self.assertEqual(original, restored)
        assert_allclose(restored.a @ restored.x, restored.b, rtol=1e-7, atol=1e-9)

    def test_json_serialization_without_work(self):
        original = Task(identifier=99, size=15)
        json_str = original.to_json()
        restored = Task.from_json(json_str)
        self.assertEqual(original, restored)
        self.assertTrue(np.allclose(restored.x, np.zeros(15)))
        self.assertEqual(restored.time, 0.0)

    def test_equality_method(self):
        t1 = Task(identifier=1, size=30)
        t1.work()

        t2 = Task(identifier=1, size=30)
        t2.a = t1.a.copy()
        t2.b = t1.b.copy()
        t2.x = t1.x.copy()
        t2.time = t1.time

        self.assertEqual(t1, t2)
        t3 = Task(identifier=2, size=30)
        t3.work()
        self.assertNotEqual(t1, t3)

    def test_equality_with_different_types(self):
        task = Task(identifier=1, size=10)
        self.assertFalse(task == "not a task")
        self.assertFalse(task is None)
        self.assertFalse(task == 42)

    def test_json_structure(self):
        task = Task(identifier=7, size=5)
        task.work()
        json_str = task.to_json()
        data = json.loads(json_str)
        required_fields = ["identifier", "size", "a", "b", "x", "time"]
        for field in required_fields:
            self.assertIn(field, data)
        self.assertEqual(len(data["a"]), 5)
        self.assertEqual(len(data["a"][0]), 5)
        self.assertEqual(len(data["b"]), 5)
        self.assertEqual(len(data["x"]), 5)


if __name__ == "__main__":
    unittest.main(verbosity=2)
