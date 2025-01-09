import os
from time import sleep
from threading import Thread

os.system('COLOR B')


class Knight(Thread):
    def __init__(self, name: str, power: int):
        super().__init__()
        self.name = name
        self.power = power

    def run(self):
        print(f"{self.name}, на нас напали!")
        fighters = 100
        i = 0

        while fighters != 0:
            i += 1
            fighters -= self.power
            sleep(1)
            print(f'{self.name}, сражается {i} день(дня)..., осталось {fighters} воинов.')

            if fighters == 0:
                print(f'{self.name} одержал победу спусня {i} дней(дня)!')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

print('Все битвы закончились!')

try:
    os.system('PAUSE')
except:
    os.system('CLS')
