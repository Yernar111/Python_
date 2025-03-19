# Pygame - библиотека которая содержит в себе множество модулей для работы с 2D играми и контентом.
# sprite - модуль для движущихся обьектов в игре
# event - модуль событии внутри игры(нажатия клавиш, мыши или других действии)
# display - модуль работы с окном игры, содержащий в себе множество 

# init - инициализирует(запускает) все модули pygame. Является первым действием которое необходимо выполнить.

# Surface - тип обьекта который присваивается каждому обьекту в игре и даже самому окну игры. Область обьекта surface дает возможность рисовать, заливать цветом эту область и т.д. 

# abcd = pygame.display.set_mode((width, height)) - создается окно и присваивается размер в пикселях, затем это окно присваивается переменной abcd который в следствии становится обьектом типа surface и тут же выводит это окно на экран.
# pygame.display.set_caption("name") - присваивание имени окну
# abcd.blit("1",("2","3")) - метод позволяет рисовать изображение на заданной позции. 1 - обьект типа surface. 2 и 3 - позиция в котором будет обьект типа surface
# pygame.display.update() - обновить окошко. Стоит выполнять в конце главной итерации или после каждого изменения контента в игре


# abcd = pygame.event.wait() - обьект который ждет(ставит на паузу) пока не произойдет событие. Лучше не использовать при анимации.
# for abcd in pygame.event.get() - возвращает список событии. Является более подходящей альтернативой pygame.event.wait() так как не ждет и не ставит на паузу игру пока не произойдет какое то событие
# if abcd.type == pygame.QUIT - условие для завершения игры. Возвращает тип события и проверяет условие

# efgh = pygame.key.get_pressed() - возвращает список нажатых клавиш. if efgh[pygame.K_q]: можно проверить нажималась ли клавиша(входит ли клавиша в список)
#
# MOUSBEBUTTONDOWN, MOUSEBUTTONUP, MOUSEMOTION - типы событии мыши (.type) 
#

# abcd = pygame.Surface((width, height)) - создание пустого обьекта surface с прописанной шириной и высотой которому можно будет в дальнейшем заполнить цветами. По умолчанию имеет прямоугольную форму
# abcd.fill((R,G,B)) - заливка обьекта surface цветом(даже всего окошка). Диапазон для каждого цвета 0-255.
# efgh = pygame.image.load("name.png") - загрузка изображения в обьект surface

# abcd = pygame.Rect(x,y,width,height) - класс для создания прямоугольника с прописанными координатами левого верхнего угла и размером

# Методы в классе Rect: 
# abcd.colliderect("name") - метод  проверяет соприкасается ли обьект класса Rect, с другим обьектом класса Rect. (Используется так же как и при работе с методами внутри классов: abcd.colliderect("name"))
# abcd.move(dx,xy) - метод перемещает обьект на заданное количество пикселей
# abcd.collidelist("name_of_list") - метод проверяет соприкасается ли обьект класса Rect с любым обьектом внутри списка класса Rect

# abcd = pygame.font.Font("название_шрифта", "размер шрифта") - класс который позволяет создать обьект для хранения надписи с определенным шрифтом и размером
# e = abcd.render("text", "сглаживание: true/false", (R,G,B)) - метод внутри класса для отрисовки текста в виде обьекта surface. 

# pygame.draw."название_фигуры"(surface, color, points, width) - позволяет добавлять рисунки геометрических фигур(line, circle, rect, polygon, ellipse). 

# abcd = pygame.image.load("название.png") - создание обьекта типа surface с изображением

# pygame.mixer.init() - инициализирует модуль(mixer) для работы со звуком
# abcd = pygame.mixer.Sound("название_звукового_файла") - создает обьект который хранит в себе звуковой файл(вызывает класс Sound внутри модуля mixer)
# abcd.play(loops=2) - воспроизведение звука(вызов метода в классе sound). Если скобки будут пустыми, то звук будет играть вечно
# abcd.stop() - остановка звука

# abcd = pygame.time.Clock() - создание обьекта принадлежащему классу Clock внутри модуля time
# abcd.tick(n) - метод внутри класса Clock который отвечает за установку количества фреймов в одну секунду(следует использовать в самом конце). Фрейм - итерация одного игрового цикла.

# efgh = abcd.get_rect() - позволяет создать обьект типа rect из обьекта типа surface(abcd). С помощью этого можно менять позицию rect
# a.blit(abcd, efgh) - отрисовка обьекта surface на позиции его rect


# pygame.quit() - завершение pygame

import pygame
import time

pygame.init()

a = pygame.display.set_mode((500, 600))
pygame.display.set_caption("first")

a.fill((0,120,0))

#d = pygame.font.Font(None, 70)
#e = d.render("text", True, (200,0,0))
#a.blit(e,(200,300))


b = pygame.image.load("clock.png")
b = pygame.transform.scale(b,(500,600))
a.blit(b,(10,20))
pygame.display.update()
#time.sleep(5)
#e = b.move(50,70)
#x,y = e.get_pos()
#a.blit(e, (x,y))



#c = pygame.Surface((400,400))
#c.fill((255,0,0))
#a.blit(c,(0,0))

time.sleep(7)
pygame.quit()
