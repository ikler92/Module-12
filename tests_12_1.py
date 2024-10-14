import unittest
from runner import Runner


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        """Тестирует метод walk класса Runner."""
        runner = Runner("Runner1")
        for _ in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50, "После 10 прогулок дистанция должна равняться 50.")

    def test_run(self):
        """Тестирует метод run класса Runner."""
        runner = Runner("Runner2")
        for _ in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100, "Дистанция после 10 пробежек должна быть 50.")

    def test_challenge(self):
        """Тестирует разницу в дистанции у двух бегунов, один из которых бегает, а другой ходит."""
        runner1 = Runner("Runner1")
        runner2 = Runner("Runner2")

        for _ in range(10):
            runner1.run()
            runner2.walk()

        self.assertNotEqual(runner1.distance, runner2.distance,
                            "Дистанция не должна быть равной после 10 прогулок и пробежек.")
