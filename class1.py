class door:
    def __init__(self, x, y): # Метод __init__ позволяет дать значение классу сразу при вызове, этот метод также называют конструктором
        self.x=x
        self.y=y
        print(self.x, self.y)

    def gain(self,abcd,z):
        self.abcd=abcd
        self.z=z

    def help(self):
        self.help2() # Внутри класса можно обращаться к функциям которые находятся внутри этого же класса
        
    def help2(self):
        print(self.abcd, self.z)

a=door("Ab", "Cd") # Вызов класса и метода __init__ с заранее прописанными значениями
a.gain("Main","Double") # вызов метода gain с значениями (Обращение к методу)
a.help() #Вывод значении
a.help2()

print(type(a)) # Выводит к какому классу принадлежит обьект
print(dir(a)) # Выводит список возможностей обьекта, элементы с нижним подчеркиванием используются самим python, остальные те переменные и методы которые мы сами создали

print()

w=[1,2,3]
print(type(w))
print(dir(w))