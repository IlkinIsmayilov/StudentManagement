from db import StudentList


class StudentManagement:
    def __init__(self, _code, _ad, _soyad, _email, _mobile):
        self.code = _code
        self.ad = _ad
        self.soyad = _soyad
        self.email = _email
        self.mobile = _mobile
        StudentList.append(self)

    def showData(self):
        print(self.code + " / " + self.ad + " / " + self.soyad + " / " + self.email + " / " + self.mobile)

    def fullShowdata(self):
        for istifadeci in StudentList:
            istifadeci.showData()
    def deleteStudent(self):
        delStud = input("Telebe kodunu yazin : ")
        for data in StudentList:
            if data.code == delStud:
                StudentList.remove(data)
                print("silindi....")

    def showStudent(self):
        showStud = input("Telebe adini yazin : ")
        for data in StudentList:
            if data.ad == showStud:
                print(data.code + " / " + data.ad + " / " + data.soyad + " / " + data.email + " / " + data.mobile)
                print("gosterildi....")

    def changeStudent(self):
        changStud = input("Telebe kodunu yazin : ")
        for data in StudentList:
            if data.code == changStud:
                print("Yeni melumatlari daxil edin : ")
                code = input("Code : ")
                ad = input("Ad : ")
                soyad = input("Soyad : ")
                email = input("Email : ")
                mobile = input("Mobile : ")
                data.code  = code
                data.ad  = ad
                data.soyad  = soyad
                data.email  = email
                data.mobile  = mobile
                print("deyisdirildi....")
