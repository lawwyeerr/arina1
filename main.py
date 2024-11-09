import random
from operator import truediv
from symbol import return_stmt
from tkinter.font import names


class pet:
     def __init__(self):
         self.hp = 100
         self.hungry = 30
         self.happy = 60
         self.energy = 60
         self.name = "Муся"
         self.species = "Киця"
mypet = pet()

class money:
    def __init__(self):
        self.m = 0
mon = money()
While True:
    feed = input("Покормити(A),Пограти(B),Вкласти спати(C)")
    if feed=="A":
      if mypet.hungry <= 40:
      mypet.hungry += 20
      mypet.happy += 10
      mon.m += 10
      print("Ви покормили свою тваринку та заробили монети", "Рівень голоду" , mypet.hungry , "Рівень щастя", mypet.happy,
            "Ваш баланс" , mon.m)

      else:
           print("Киця не голодна")
    if feed=="B":
      if mypet.energy >= 50:
           mypet.energy -= 20
           mypet.happy += 10
           mon.m += 20
       print("Ви пограли з кицею", "Рівень енергії", mypet.energy , "Рівень щастя" , mypet.happy ,
             "Ваш баланс", mon.m)
       else:
           print("Киця заморилась")

    if feed=="C":
       if mypet.energy >= 30:
        mypet.energy += 30
        mypet.happy += 20
        mon.m +=20
        print("Ви поклали кицю спать" , "Рівень енергії" , mypet.energy ,"Рівень щастя" , mypet.happy, "Ваш баланс", mon.m  )


