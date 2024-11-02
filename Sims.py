import random

class Human:
    def __init__(self, name="Niger", job=None, home=None, car=None):
        self.name = name
        self.home = home
        self.job = job
        self.car = car
        self.money = 100
        self.gladness = 50
        self.satiety = 50

    def get_home(self):
        self.home = House()

    def get_car(self):
        self.car = Auto(brands_of_car)

    def get_job(self):
        if self.car.drive():
            pass
        else:
            self.to_repair()
            return
        self.job = Job(job_list)

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
        if self.car.drive():
            pass
        else:
            if self.car.fuel < 20:
                self.shopping('fuel')
                return
            else:
                self.to_repair()
                return
            self.money += self.job.salary
            self.gladness -= self.job.gladness_less
            self.satiety -= 4

    def shopping(self, manage):
        if self.car.drive():
            pass
        else:
            if self.car.fuel < 20:
                self.shopping('fuel')
                return
            else:
                self.to_repair()
                return
        if manage == 'fuel':
            print('I bought fuel')
            self.money -= 100
            self.car.fuel += 5
        elif manage == 'food':
            print('I bought food')
            self.money -= 50
            self.home.food += 50
        elif manage == "Eggs":
            print('EEEEEEGGGGGSSSSS')
            self.gladness += 10
            self.satiety += 2
            self.money -= 50



    def chill(self):
        self.gladness += 16
        self.home.mess += 5

    def clean_house(self):
        self.gladness -=5
        self.home.mess = 0

    def to_repair(self):
        self.car.streght += 100
        self.money -= 50


    def day_index(self, day):
        day = f"Today the {day} of {self.name}`s life!"
        print(f"{day:=^50}","\n")

        human_index = self.name + "`s indexes"
        print(f"{human_index:=^50}","\n")
        print(f"Money - {self.money}")
        print(f"Satiety - {self.satiety}")
        print(f"Gladness - {self.gladness}")

        home_index = "Home index"
        print(f"{home_index:=^50}","\n")
        print(f"Food - {self.home.food}")
        print(f"Strenght - {self.home.mess}")

        car_index = f"{self.car.brand} car indexes"
        print(f"{car_index:-^50}","\n")
        print(f"Fuel - {self.car.fuel}")
        print(f"Strenght - {self.car.strenght}")

    def is_alive(self):
        if self.gladness < 0:
            print("Depresion...")
            return False
        if self.satiety < 0:
            print("Dead...")
            return False
        if self.money < -500:
            print('ЛОХ + БОМЖ')
            return False


    def live(self, day):
        if self.is_alive() == False:
            return False
        if self.home is None:
            print("БОМЖАРАА ААХАХАХ")
            self.get_home()
        if self.car is None:
            self.get_car()
            print("Ну і тачка...")
        if self.job is None:
            self.get_job()
            print(f'I don`t have a job, going to get job{self.car.brand}')
        self.day_index(day)

        dice = random.randint(1, 4)
        if self.satiety < 20:
            print('I`ll go to eat')
            self.eat()
        elif self.gladness < 20:
            if self.home.mess > 15:
                print("I want to chill, but there so much mess ... so i cleanmy house!")
                self.clean_house()
            else:
                print("Let`s chill")
                self.chill()
        elif self.money < 0:
            print("Start working!")
            self.work()
        elif self.car.strenght < 15:
            print("i need to repair my car")
            self.to_repair()
        elif dice == 1:
            print('I will chill!')
            self.chill()
        elif dice == 2:
            print("Start working!")
            self.work()
        elif dice == 3:
            print('I want to clear my house')
            self.clean_house()
        elif dice == 4:
            print('I NEED ЯЯЯЯЯЄЄЄЧЧКААА')
            self.shopping(manage='eggs')



brands_of_car = {
    "BMW":{"fuel":100, "strenght":100, "consumption":6},
    "Lada":{"fuel":50, "strenght":40, "consumption":10},
    "Volvo":{"fuel":70, "strenght":150, "consumption":8},
    "Ferrari":{"fuel":80, "strenght":128, "consumption":14},
}

class Auto:
    def __init__(self, brand_list):
        self.brand = random.choice(list(brand_list))
        self.fuel = brand_list[self.brand]["fuel"]
        self.strenght = brand_list[self.brand]["strenght"]
        self.consumption = brand_list[self.brand]["consumption"]

    def drive(self):
        if self.strenght > 0 and self.fuel >= self.consumption:
            self.fuel -= self.consumption
            self.strenght -= 1
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
    "Java Developer":{"salary":50, "gladness_less":13},
    "Python Developer":{"salary":40, "gladness_less":1-1},
    "C++ Developer":{"salary":45, "gladness_less":100000000000^10},
    "Ruby Developer":{"salary":70, "gladness_less":1}
}
Niger = Human(name='Niger')

for day in range(1,8):
    if Niger.live(day) == False:
        break