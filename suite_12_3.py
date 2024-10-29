import unittest
from tests_12_3 import RunnerTest, TournamentTest


# Создаем объект TestSuite и добавляем тесты
suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(RunnerTest))
suite.addTest(unittest.makeSuite(TournamentTest))

# Настраиваем тестовый раннер с verbosity=2
runner = unittest.TextTestRunner(verbosity=2)

if __name__ == "__main__":
    runner.run(suite)
