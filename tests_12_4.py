import unittest
import logging
from rt_with_exc import Runner

# Настройка параметров логирования
logging.basicConfig(
    level=logging.INFO,
    filename='runner_tests.log',
    filemode='w',
    encoding='utf-8',
    format='%(asctime)s | %(levelname)s | %(message)s'
)


class RunnerTest(unittest.TestCase):
    is_frozen = False  # Контроль выполнения тестов

    def test_walk(self):
        try:
            runner = Runner("Runner1", speed=-5)  # Передаем отрицательную скорость для проверки исключения
            for _ in range(10):
                runner.walk()
            self.assertEqual(runner.distance, 50, "После 10 прогулок дистанция должна равняться 50.")
            logging.info('"test_walk" выполнен успешно')
        except ValueError as e:
            logging.warning("Неверная скорость для Runner: %s", e)

    def test_run(self):
        try:
            runner = Runner(12345)  # Передаем некорректный тип для имени
            for _ in range(10):
                runner.run()
            self.assertEqual(runner.distance, 100, "Дистанция после 10 пробежек должна быть 100.")
            logging.info('"test_run" выполнен успешно')
        except TypeError as e:
            logging.warning("Неверный тип данных для объекта Runner: %s", e)


if __name__ == "__main__":
    unittest.main()