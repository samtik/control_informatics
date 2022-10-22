import os
def ch(n):
    for i in range(len(n)):
        n[i] = str(n[i]).strip()
def section():
    print("=" * 40)
    print("=" * 40)
def so(d):
    a = []
    d2 = []
    for i in d:
        a.append(str(i).split(",")[2][1:])
    a.sort()
    k = 1
    for i in a:
        for j in d:
            if i in j:
                d2.append(str(k) + j[1:])
                k += 1
    return d2
def change(f, n, sch):
    fileCH = open(f, "r")
    date = fileCH.readlines()
    ch(date)
    date[n-1] = "1, " + sch
    date = so(date)
    fileD = open(f, "w")
    for i in date:
        if i == date[-1]:
            fileD.write(i)
        else:
            fileD.write(i + '\n')
    fileD.close()
    section()
    print(*date, sep="\n")
def add(f, s):
    fileADD = open(f, "r")
    date = fileADD.readlines()
    ch(date)
    date.append("1, " + s)
    date = so(date)
    fileRes = open(f, "w")
    for i in date:
        if i == date[-1]:
            fileRes.write(i)
        else:
            fileRes.write(i + '\n')
    fileRes.close()
    section()
    print(*date, sep="\n")
def delete(f, n):
    fileDel = open(f, "r")
    date = fileDel.readlines()
    ch(date)
    del date[n - 1]
    date = so(date)
    fileRes = open(f, "w")
    for i in date:
        if i == date[-1]:
            fileRes.write(i)
        else:
            fileRes.write(i + '\n')
    fileRes.close()
    section()
    print(*date, sep="\n")
fl1 = True
while fl1:
    print("Check - Посмотреть список блокнотов")
    print("Create - Создать свой блокнот")
    action1 = input().lower()
    fl2 = True
    if action1 == "check":
        section()
        print("Существующие следующие блокноты:")
        print(*[i for i in os.listdir() if i[-3:] == "csv"], sep=", ")
        section()
        note = input("Выберите блокнот...\n").lower()
        section()
        while fl2:
            try:
                file = open(note)
                print(file.read())
                file.close()
                section()
                action2 = input("Выберите действие для блокнота: 1 - Изменить блокнот, 2 - Удалить блокнот\n")
                section()
                if action2 == "1":
                    action3 = input("Выберите действие для строки: 1 - Изменить строку, 2 - Добавить строку, 3 - Удалить строку\n")
                    section()
                    if action3 == "1":
                        number = int(input("Введите номер строки...\n"))
                        section()
                        strokaCH = input("Введите текст, на который меняем строку(задача, время, дата, приоритет, статус)...\n")
                        change(note, number, strokaCH)
                    if action3 == "2":
                        strokaADD = input("Введите строку, которую добавляем(задача, время, дата, приоритет, статус)...\n")
                        add(note, strokaADD)
                    if action3 == "3":
                        number = int(input("Введите номер строки, которую удаляем...\n"))
                        delete(note, number)
                if action2 == "2":
                    os.remove(note)
                    print("Блокнот удален :(")
                    fl2 = False
                    break
            except:
                print("Введите назвение блокнота правильно :D")
            section()
            pr = input("Продолжить редактировать блокнот? (1 - Да, 2 - Нет)\n")
            if pr == "2":
                fl2 = False
    elif action1 == "create":
        section()
        name = str(input("Придумайте название блокнота\n"))
        section()
        sn = input("Введите строку, которую добавляем(задача, время, дата, приоритет, статус)...\n")
        newFile = open(f"{name}.csv", "w+")
        newFile.write("1, " + sn)
        newFile.close()
        file = open(f"{name}.csv")
        print(file.read())
        file.close()
        section()
        print("Блокнот создан :D")
    section()
    res = input("Продолжить работать с блокнотами? (1 - Да, 2 - Нет)\n")
    if res == "2":
        fl1 = False
