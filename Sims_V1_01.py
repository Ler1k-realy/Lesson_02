import random


class Human:
    def __init__(self, name="Niger", job=None, home=None, car=None, country=None):
        self.name = name
        self.home = home
        self.job = job
        self.car = car
        self.country = country
        self.money = 100
        self.gladness = 50
        self.satiety = 50
        self.chance_to_die = 0

    def get_home(self):
        self.home = House()

    def get_car(self):
        self.car = Auto(brands_of_car)

    def get_country(self):
        country_obj = Country_live(country_list)
        self.country = country_obj.country
        self.chance_to_die = country_obj.chance_to_die

    def get_job(self):
        if self.car and self.car.drive():
            pass
        else:
            self.to_repair()
            return
        self.job = Job(job_list)

    def die(self):
        if self.country == "Gaza":
            self.chance_to_die += random.randint(20, 45)
        elif self.country == "Ukraine":
            self.chance_to_die += random.randint(5, 15)
        elif self.country == "China":
            self.chance_to_die += random.randint(1, 3)
        elif self.country == "USA":
            self.chance_to_die += random.randint(1, 3)
        elif self.country == "North Korea":
            self.chance_to_die += random.randint(10, 20)

    def eat(self):
        if self.home.food <= 3:
            self.shopping("food")
        else:
            if self.satiety >= 100:
                self.satiety = 100
                return
            self.satiety += 5
            self.home.food -= 5

    def work(self):
        if self.car and self.car.drive():
            if self.car.fuel < 20:
                self.shopping('fuel')
                return
            if self.job:
                self.money += self.job.salary
                self.gladness -= self.job.gladness_less
                self.satiety -= 4
        else:
            self.to_repair()

    def shopping(self, manage):
        if self.car and self.car.drive():
            if manage == 'fuel':
                print('I bought fuel')
                self.money -= 100
                self.car.fuel += 5
            elif manage == 'food':
                print('I bought food')
                self.money -= 50
                self.home.food += 50
            elif manage == "eggs":
                print('EEEEEEGGGGGSSSSS')
                self.gladness += 10
                self.satiety += 2
                self.money -= 50
        else:
            if self.car and self.car.fuel < 20:
                self.shopping('fuel')
            else:
                self.to_repair()

    def chill(self):
        self.gladness += 16
        self.home.mess += 5

    def clean_house(self):
        self.gladness -= 5
        self.home.mess = 0

    def to_repair(self):
        if self.car:
            self.car.strength += 100
            self.money -= 50

    def day_index(self, day):
        print(f"{f'Today the {day} of {self.name}`s life!':=^50}")
        print(f"{f'{self.name}`s indexes':=^50}")
        print(f"Money - {self.money}")
        print(f"Satiety - {self.satiety}")
        print(f"Gladness - {self.gladness}")
        print(f"Country - {self.country}")
        print(f"Chance to die - {self.chance_to_die}")
        print(f"Food - {self.home.food}")
        print(f"Mess - {self.home.mess}")
        print(f"{self.car.brand} car indexes".center(50, "-"))
        print(f"Fuel - {self.car.fuel}")
        print(f"Strength - {self.car.strength}")

    def is_alive(self):
        if self.gladness < 0:
            print("Depression...")
            return False
        if self.satiety < 0:
            print("Dead...")
            return False
        if self.money < -500:
            print('No money left...')
            return False
        if self.chance_to_die >= 150:
            print('You were killed')
            return False
        return True

    def live(self, day):
        if not self.is_alive():
            return False
        if self.home is None:
            print("No home...")
            self.get_home()
        if self.car is None:
            self.get_car()
            print("No car...")
        if self.job is None:
            self.get_job()
            print(f'I don`t have a job, going to get a job at {self.car.brand}')
        if self.country is None:
            self.get_country()
            print('I want to live in a country')

        
        self.die()

        self.day_index(day)

        dice = random.randint(1, 4)
        if self.satiety < 20:
            print('I`ll go to eat')
            self.eat()
        elif self.gladness < 20:
            if self.home.mess > 15:
                print("I want to chill, but there is too much mess ... cleaning up!")
                self.clean_house()
            else:
                print("Let`s chill")
                self.chill()
        elif self.money < 0:
            print("Start working!")
            self.work()
        elif self.car and self.car.strength < 15:
            print("I need to repair my car")
            self.to_repair()
        elif dice == 1:
            print('I will chill!')
            self.chill()
        elif dice == 2:
            print("Start working!")
            self.work()
        elif dice == 3:
            print('I want to clean my house')
            self.clean_house()
        elif dice == 4:
            print('I need eggs!')
            self.shopping(manage='eggs')

        return True


brands_of_car = {
    "BMW": {"fuel": 100, "strength": 100, "consumption": 6},
    "Lada": {"fuel": 50, "strength": 40, "consumption": 10},
    "Volvo": {"fuel": 70, "strength": 150, "consumption": 8},
    "Ferrari": {"fuel": 80, "strength": 128, "consumption": 14},
}


class Auto:
    def __init__(self, brand_list):
        self.brand = random.choice(list(brand_list))
        self.fuel = brand_list[self.brand]["fuel"]
        self.strength = brand_list[self.brand]["strength"]
        self.consumption = brand_list[self.brand]["consumption"]

    def drive(self):
        if self.strength > 0 and self.fuel >= self.consumption:
            self.fuel -= self.consumption
            self.strength -= 1
            return True
        else:
            print("The car cannot move")
            return False


class House:
    def __init__(self):
        self.mess = 0
        self.food = 0


class Job:
    def __init__(self, job_list):
        self.job = random.choice(list(job_list))
        self.salary = job_list[self.job]['salary']
        self.gladness_less = job_list[self.job]["gladness_less"]


job_list = {
    "Java Developer": {"salary": 50, "gladness_less": 13},
    "Python Developer": {"salary": 40, "gladness_less": 1},
    "C++ Developer": {"salary": 45, "gladness_less": 10},
    "Ruby Developer": {"salary": 70, "gladness_less": 1}
}


class Country_live:
    def __init__(self, country_list):
        self.country = random.choice(list(country_list))
        self.chance_to_die = country_list[self.country]["chance to die"]


country_list = {
    "Gaza": {"chance to die": 45},
    "Ukraine": {"chance to die": 10},
    "China": {"chance to die": 1},
    "USA": {"chance to die": 1},
    "North Korea": {"chance to die": 25}
}

Niger = Human(name='Niger')
for day in range(1, 8):
    if not Niger.live(day):
        break
