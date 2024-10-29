import unittest
from runner_and_tournament import Tournament, Runner


def freeze_check(func):
    """Декоратор, который пропускает тесты, если атрибут is_frozen установлен в True."""

    def wrapper(self, *args, **kwargs):
        if getattr(self, 'is_frozen', False):
            self.skipTest("Тесты в этом кейсе заморожены")
        else:
            func(self, *args, **kwargs)

    return wrapper


class RunnerTest(unittest.TestCase):
    is_frozen = False  # Контроль выполнения тестов

    @freeze_check
    def test_walk(self):
        runner = Runner("Runner1")
        for _ in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50, "После 10 прогулок дистанция должна равняться 50.")

    @freeze_check
    def test_run(self):
        runner = Runner("Runner2")
        for _ in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100, "Дистанция после 10 пробежек должна быть 100.")

    @freeze_check
    def test_challenge(self):
        runner1 = Runner("Runner1")
        runner2 = Runner("Runner2")
        for _ in range(10):
            runner1.run()
            runner2.walk()
        self.assertNotEqual(runner1.distance, runner2.distance,
                            "Дистанция не должна быть равной после 10 прогулок и пробежек.")


class TournamentTest(unittest.TestCase):
    is_frozen = True  # Заморозка тестов для TournamentTest

    @freeze_check
    def test_first_tournament(self):
        usain = Runner("Усэйн", 10)
        nick = Runner("Ник", 3)
        tournament = Tournament(90, usain, nick)
        results = tournament.start()
        last_runner = results[max(results.keys())]
        self.assertTrue(last_runner == "Ник")

    @freeze_check
    def test_second_tournament(self):
        andrey = Runner("Андрей", 9)
        nick = Runner("Ник", 3)
        tournament = Tournament(90, andrey, nick)
        results = tournament.start()
        last_runner = results[max(results.keys())]
        self.assertTrue(last_runner == "Ник")

    @freeze_check
    def test_third_tournament(self):
        usain = Runner("Усэйн", 10)
        andrey = Runner("Андрей", 9)
        nick = Runner("Ник", 3)
        tournament = Tournament(100, usain, andrey, nick)
        results = tournament.start()
        last_runner = results[max(results.keys())]
        self.assertTrue(last_runner == "Ник")
