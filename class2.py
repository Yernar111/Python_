class hang:
    def __init__(self, a, b):
        self.a=a
        self.b=b
    def out(self):
        print(self.a, self.b)


class left(hang): # Для обьвления дочернего класса, надо в скобках написать название родительского класса. Созданный класс будет наследовать свойства родительского
    def __init__(self, x, y):
        self.a=x # Созданный класс наследует названия полей(переменных) родительского класса
        self.b=y

class right(hang):
    def __init__(self, a, b):
        hang.__init__(self, a, b) # Благодаря этой функции можно продолжить наследовать соответствующую функцию с родительского класса
        print(self.a, self.b)

class mid(hang):
    def __init__(self, a, b):
        super().__init__(a, b) # Наследует все свойства родительского класса


won=hang("Abcd", "Efgh")
won.out()

life=left("Q", True)
life.out()

head=mid("will", 123)
head.out()