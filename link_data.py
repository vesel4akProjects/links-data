import json #импортируем библиотеку json для работы с файлами формата json
def open_file(link): #функция для открытия файла
    with open(link,"r") as file:
        links =set(file.read().splitlines())
    return links
def write_file(links,link): #функция для изменения  файла
    with open(link,"w",encoding ="utf-8") as file:
        file.write("\n".join(links))
def open_json(jsfile):      #функция для открытия файла с помощью json
    with open(jsfile,"r",encoding ="utf-8") as json_file:
        load = json.load(json_file)
    return load
def write_json(data,jsfile): #функция для изменения  файла с помощью json
    with open(jsfile,"a",encoding ="utf-8") as jsonfile:
        json.dump(data,jsonfile)
def sort(link1,link2): #функция для перебора ссылкок
    found =set()
    not_found =set()
    for link in link1:
         if link in link2:
            found.add(link)
         else:
            not_found.add(link)
    for link in link2:
        if link not in link1:
            not_found.add(link)
    write_json(list(found),"совпадения.json") #запускаем цикл программы для размещения ссылок по файлам
    write_json(list(not_found), "не_найдено.json")

link1 = open_file("Ссылки1.txt") #ссылка №1
link2 = open_file("Ссылки2.txt") #ссылка №2
sort(link1,link2) #сортировка
