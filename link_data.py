import json #import json
def open_file(link): #func
    with open(link,"r") as file:
        links =set(file.read().splitlines())
    return links
def write_file(links,link): #func
    with open(link,"w",encoding ="utf-8") as file:
        file.write("\n".join(links))
def open_json(jsfile):      #func
    with open(jsfile,"r",encoding ="utf-8") as json_file:
        load = json.load(json_file)
    return load
def write_json(data,jsfile): #func
    with open(jsfile,"a",encoding ="utf-8") as jsonfile:
        json.dump(data,jsonfile)
def sort(link1,link2): #func
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
    write_json(list(found),"совпадения.json") #launch
    write_json(list(not_found), "не_найдено.json")

link1 = open_file("links1.txt") #link1
link2 = open_file("links2.txt") #link2
sort(link1,link2) #sort
