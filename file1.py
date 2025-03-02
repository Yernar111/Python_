a = open("text1", "r") # r(read)- режим открытия файла для чтения. open() это класс внутри которого есть метод read(). То есть мы создаем переменную (обьект), и этот обьект принадлежит классу open() 
#print(a, end="\n\n") # Попытка вывести обьект в котором открыт файл не приведет к чтению содержимого файла
#for i in a:
#    print(i, end="") # Обьект в котором хранится файл также можно рассматривать как последовательность строк, и к каждой строке можно получить доступ с помощью цикла

b=a.read(7) # Можно дать переменной метод чтения целого файл, это позволит вывести весь текст в файле(не работает если текст файла уже использовался ранее). Также можно вывести определенное колво символов в текстовом файле введя число внутри скобок
print(b)
a.close()

c=open("text2", "w") # w(write)- режим открытия файла для написания данных. Если файла с таким именем нет, то автоматический создается новый файл.
# write() позволяет записывать данные внутрь файла. При этом данные написанные ранее заменяются текущими.
c.write("Contrary to popular belief,\nLorem Ipsum is not simply random text.\nIt has roots in a piece of classical Latin literature from 45 BC,\nmaking it over 2000 years old.")
c.close()

d=open("text2", "r")
print(d.readline(), end="") # readline() метод позволяющий читать текущую(первую) строку. Кол-во прочитанных строк зависит от количества вызовов этого метода
print(d.readline(), end="")
print(d.readline(), end="")
print(d.readline(), end="")
d.close()

e=open("text2", "a") # a(append) - режим открытия файла для добавления данных. Если файла с таким именем нет, то автоматический создается новый файл.
e.write("\nContent here") # Записывание данных внутрь файла, с сохранением данных записанных ранее.
e.close()

f=open("text2", "r")
print(f.read())
f.close()

