class Human:
    def eat(self):
        print("I can eat")
    def work(self):
        print("I can work")
class Male(Human):
    def flirt(self):
        print("I can code")
        super().work()
male_1=Male()
male_1.work()
male_1.flirt()