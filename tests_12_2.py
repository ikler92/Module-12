import unittest
from runner_and_tournament import Runner, Tournament


class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}  # Словарь для сохранения результатов всех тестов

    def setUp(self):
        # Создаём бегунов
        self.usain = Runner("Усэйн", 10)
        self.andrey = Runner("Андрей", 9)
        self.nick = Runner("Ник", 3)

    @classmethod
    def tearDownClass(cls):
        # Выводим результаты всех тестов
        for test_name, result in cls.all_results.items():
            formatted_result = {place: str(runner) for place, runner in result.items()}
            print(f"{formatted_result}")

    def test_usain_and_nick(self):
        # Участвуют Усэйн и Ник
        tournament = Tournament(90, self.usain, self.nick)
        results = tournament.start()
        TournamentTest.all_results['test_usain_and_nick'] = results

        # Проверяем, что Ник последний
        last_runner = results[max(results.keys())]
        self.assertTrue(last_runner == "Ник")

    def test_andrey_and_nick(self):
        # Участвуют Андрей и Ник
        tournament = Tournament(90, self.andrey, self.nick)
        results = tournament.start()
        TournamentTest.all_results['test_andrey_and_nick'] = results

        # Проверяем, что Ник последний
        last_runner = results[max(results.keys())]
        self.assertTrue(last_runner == "Ник")

    def test_usain_andrey_nick(self):
        # Участвуют Усэйн, Андрей и Ник
        tournament = Tournament(100, self.usain, self.andrey, self.nick)
        results = tournament.start()
        TournamentTest.all_results['test_usain_andrey_nick'] = results

        # Проверяем, что Ник последний
        last_runner = results[max(results.keys())]
        self.assertTrue(last_runner == "Ник")


if __name__ == '__main__':
    unittest.main()
