import logging


logging.basicConfig(
    level=logging.INFO,
    filename='runner_tests.log',
    filemode='w',
    encoding='utf-8',
    format='%(asctime)s - %(levelname)s - %(message)s'
)


class Runner:
    def __init__(self, name, speed=5):
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError(f'Имя может быть только строкой, передано {type(name).__name__}')
        self.distance = 0
        if speed > 0:
            self.speed = speed
        else:
            raise ValueError(f'Скорость не может быть отрицательной, сейчас {speed}')

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name



class RunnerTest:
    def test_walk(self):
        try:
           
            runner = Runner('Тест', speed=-5)
            runner.walk()
            logging.info('"test_walk" выполнен успешно')
        except ValueError as e:
            logging.warning(f'Неверная скорость для Runner: {e}')

    def test_run(self):
        try:

            runner = Runner(123, speed=5)
            runner.run()
            logging.info('"test_run" выполнен успешно')
        except TypeError as e:
            logging.warning(f'Неверный тип данных для объекта Runner: {e}')



tests = RunnerTest()
tests.test_walk()
tests.test_run()


with open('runner_tests.log', 'r', encoding='utf-8') as log_file:
    log_contents = log_file.read()

log_contents
