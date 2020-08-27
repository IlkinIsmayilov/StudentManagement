from db import StudentList
from lib import StudentManagement


def check():
    say = input("telebe sayini yazin : ")
    if say.isdigit():
        i = 1
        while i <= int(say):
            code = input("Code : ")
            ad = input("Ad : ")
            soyad = input("Soyad : ")
            email = input("Email : ")
            mobile = input("Mobile : ")
            global student
            student = StudentManagement(code, ad, soyad, email, mobile)
            print(i, ". telebe elave edildi")
            i += 1
    else:
        print("reqem daxil etmek lazimdir")
        check()


def chooseYN():
    YN = input("davam etmek isteyirsiz? y/n : ")
    if YN == "y":
        chooseItem()
    elif YN == "n":
        print("proqramdan cixis edildi...")


def chooseItem():
    print(""" 
    Enter 1 : Butun telebeleri goster 
    Enter 2 : Yeni telebe elave et
    Enter 3 : Telebe sil 
    Enter 4 : Telebe melumatini deyisdir
    Enter 4 : Telebe adina gore melumatlari goster""")
    choose = input(" Bir secim edin  : ")
    if choose == "1":
        if StudentList == []:
            print(StudentList)
        else:
            print(student.fullShowdata())
        chooseYN()
    elif choose == "2":
        check()
        chooseYN()
    elif choose == "3":
        # telebe koduna gore melumatlarin silinmesi
        student.deleteStudent()
        chooseYN()
    elif choose == "4":
        # telebe koduna gore melumatlari deyisdirilmesi
        student.changeStudent()
        chooseYN()
    elif choose == "5":
        # telebe adina gore melumatlarin gosterilmesi
        student.showStudent()
        chooseYN()

