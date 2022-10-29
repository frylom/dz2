import random


class Cat:
    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.satiety = 10
        self.caress = 10
        self.alive = True

    def to_eat(self):
        print('Time to eat!')
        self.satiety += 0.12
        self.gladness -= 3

    def to_sleep(self):
        print('Its time to sleep^')
        self.gladness += 3

    def to_chill(self):
        print('Its time to rest!')
        self.satiety -= 0.1
        self.gladness += 5

    def is_alive(self):
        if self.satiety < -0.5:
            print('Hunger....')
            self.alive = False
        elif self.gladness <= 0:
            print('Depression...')
            self.alive = False
        elif self.satiety > 5:
            print('Im happy than I was stoked!')
            self.alive = True

    def end_of_day(self):
        print(f'Gladness = {self.gladness}')
        print(f'Progress of caress = {round(self.caress, 2)}')

    def live(self, day):
        day = 'Day ' + str(day) + ' of ' + self.name + ' live'
        print(f"{day:=^50}")
        live_cube = random.randint(1, 3)
        if live_cube == 1:
            self.to_eat()
        elif live_cube == 2:
            self.to_sleep()
        elif live_cube == 3:
            self.to_chill()
        self.end_of_day()
        self.is_alive()

steve = Cat(name='Steve')

for day in range(7300):
    if steve.alive == False:
        break
    steve.live(day)