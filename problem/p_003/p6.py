import random

class Person:

    def __init__(self):
        self.health = 10
        self.maxHp = self.health * 10
        self.hp = self.maxHp
        self.money = 10

    def work(self):
        ran = random.randint(5,20)
        self.hp = self.hp - ran
        self.money += ran
        print("[System]일을 합니다.")

    def exercise(self):
        ran = random.randint(1,3)
        self.health += ran
        self.money -= (ran*5)
        print("[System]운동을 합니다.")

    def sleep(self):
        ran = random.randint(10,20)
        self.hp = self.hp + ran
        print("[System]잠을 잡니다.")

class Warior(Person):
    def __init__(self):
        super().__init__()
        self.exp = 0
    
    def war(self):
        ran = random.randint(1,10)
        self.hp -= 10
        self.exp += ran
        print("[System]사냥을 합니다.")
    

person = Warior()
print("Money :", person.money)
print("Hp :",person.hp)
person.work()
print("Money :", person.money)
print("Hp :",person.hp)
person.exercise()
print("Money :", person.money)
print("Hp :",person.hp)
person.sleep()
print("Money :", person.money)
print("Hp :",person.hp)
person.war()
print("Hp :", person.hp)
print("EXP :",person.exp)
person.war()
print("Hp :", person.hp)
print("EXP :",person.exp)