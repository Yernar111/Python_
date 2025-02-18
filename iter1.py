# Работа с итераторами внутри класса
class hand:
  def __iter__(self):
    self.a = 2
    return self
  
  def __next__(self):
    t=self.a
    self.a+=2
    return t


val=hand()
val.__iter__() # Вызов обьекта итератора и переменной внутри класса
print(val.__next__()) # Вызов метода __next__
print(val.__next__())
print()

h=iter(val) # Присваеиваем переменной обьект итератора
print(next(h)) # Переменная играет роль итератора
print(next(h)) 