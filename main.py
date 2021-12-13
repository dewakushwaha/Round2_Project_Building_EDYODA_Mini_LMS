import datetime
from datetime import date


class Module():
    def __init__(self):
        self.M_id = [101, 102, 103, 104]
        self.M_name = ['Python', 'DSA Basics', 'MySQL', 'Data Analysis']
        self.M_start_date = [date(2021, 11, 10),
                             date(2021, 12, 2),
                             date(2022, 1, 1),
                             date(2022, 1, 26)]
        self.M_end_date = [date(2021, 12, 1),
                           date(2021, 12, 31),
                           date(2022, 1, 25),
                           date(2022, 2, 15)]

    def create_module(self):
        M_id = int(input('Enter the id'))
        self.M_id.append(M_id)
        M_name = input('Enter module name')
        self.M_name.append(M_name)
        M_start_date = input(datetime.date)
        self.M_start_date.append(M_start_date)
        M_end_date = input(datetime.date)
        self.M_end_date.append(M_end_date)

    def view_module_details(self):
        length = len(self.M_id)
        for i in range(length):
            print("\nModule ID:", self.M_id[i])
            print("\nModule Name:", self.M_name[i])
            print("\nModule Start date:", self.M_start_date[i])
            print("\nModule End date:", self.M_end_date[i])
            print("---------------------------------------------")

    def update_module(self):
        id = int(input("Enter the module id which you want to Update"))
        length = len(self.M_id)
        for i in range(length):
            if (self.M_id[i] == id):
                index = i
                break

        print("-------------------YOUR MODULE----------------------")
        print("\nModule ID:", self.M_id[index])
        print("\nModule Name:", self.M_name[index])
        print("\nModule Start date:", self.M_start_date[index])
        print("\nModule End date:", self.M_end_date[index])

        print("-------------------ENTER NEW VALUES YOU WANT TO UPDATE----------------------")
        self.M_id[index] = int(input('Enter the id'))
        self.M_name[index] = input('Enter module name')
        self.M_start_date[index] = input(datetime.date)
        self.M_end_date[index] = input(datetime.date)

        print("Successfully UPDATED!!!!!")

    def delete_module(self):
        id = int(input("Enter the module id which you want to delete"))
        length = len(self.M_id)
        for i in range(length):
            if (self.M_id[i] == id):
                index = i
                break

        del self.M_id[index]
        del self.M_name[index]
        del self.M_start_date[index]
        del self.M_end_date[index]
        print("Successfully deleted!!!!!")


class Unit(Module):
    def __init__(self):
        self.U_start_date = {101: [date(2021, 11, 10), date(2021, 11, 16), date(2021, 11, 23)],
                             102: [date(2021, 12, 2), date(2021, 12, 12), date(2021, 12, 21)],
                             103: [date(2022, 1, 1), date(2022, 1, 9), date(2022, 1, 19)],
                             104: [date(2022, 1, 26), date(2022, 2, 1), date(2022, 2, 9)]}
        self.U_end_date = {101: [date(2021, 11, 15), date(2021, 11, 22), date(2021, 12, 1)],
                           102: [date(2021, 12, 11), date(2021, 12, 20), date(2021, 12, 31)],
                           103: [date(2022, 1, 8), date(2022, 1, 18), date(2022, 1, 25)],
                           104: [date(2022, 1, 31), date(2022, 2, 8), date(2022, 2, 15)]}
        self.title = {101: ['Data types', 'Functions', 'Object Oriented Programing'],
                      102: ['Stacks', 'Queues', 'Linked List'],
                      103: ['Tables|Queries', 'SQL Queries', 'Normalization'],
                      104: ['Understanding of Data', 'Power Query for Data Analysis', 'Power BI']}

    def Create_unit(self):
        M_no = int(input("Enter module Id In which you want to create unit"))
        unit_name = input("Enter the unit name:")
        self.title[M_no].append(unit_name)
        U_start_date = input(datetime.date)
        self.U_start_date[M_no].append(U_start_date)
        U_end_date = input(datetime.date)
        self.U_end_date[M_no].append(U_end_date)

    def View_units(self):
        Module.__init__(self)
        L_module = len(self.M_id)

        for i in range(L_module):
            print("\n\n**********Module {0} Units**********".format(self.M_id[i]))
            L_Unit = len(self.title[self.M_id[i]])
            for j in range(L_Unit):
                print("Unit name:", self.title[self.M_id[i]][j])
                print("Start Date:", self.U_start_date[self.M_id[i]][j])
                print("End Date:", self.U_end_date[self.M_id[i]][j])
                print("    --------------------")

    def Update_unit(self):
        Module.__init__(self)
        L_module = len(self.M_id)

        for i in range(L_module):
            print("\nModule--->{0} Units".format(self.M_id[i]))

        m_id = int(input("Which Module Unit you want to update:"))

        L_Unit = len(self.title[m_id])
        for j in range(L_Unit):
            print("Unit ID:", j)
            print("Unit name:", self.title[m_id][j])
            print("Start Date:", self.U_start_date[m_id][j])
            print("End Date:", self.U_end_date[m_id][j])
            print("------------------------------")

        id = int(input("Which unit you want to update , enter the Unit Id"))

        print("****Enter new Values****")
        unit_name = input("Enter the unit name:")
        self.title[m_id][id] = unit_name
        U_start_date = input(datetime.date)
        self.U_start_date[m_id][id] = U_start_date
        U_end_date = input(datetime.date)
        self.U_end_date[m_id][id] = U_end_date

        print("Successfully Updated!!!!")

    def Delete_unit(self):
        Module.__init__(self)
        L_module = len(self.M_id)

        for i in range(L_module):
            print("\nModule--->{0} Units".format(self.M_id[i]))

        m_id = int(input("Which Module Unit you want to delete:"))

        L_Unit = len(self.title[m_id])
        for j in range(L_Unit):
            print("Unit ID:", j)
            print("Unit name:", self.title[m_id][j])
            print("Start Date:", self.U_start_date[m_id][j])
            print("End Date:", self.U_end_date[m_id][j])
            print("------------------------------")

        id = int(input("Which unit you want to delete , enter the Unit Id"))

        del self.title[m_id][id]
        del self.U_start_date[m_id][id]
        del self.U_end_date[m_id][id]

        print("Successfully Deleted!!!!")


class Students():
    def __init__(self):
        self.Full_Name = []
        self.Mobile_No = []
        self.Email = []
        self.Password = []
        self.ModuleID = []

    def Create_Student(self):
        Full_Name = input("Enter student full name")
        self.Full_Name.append(Full_Name)
        Mobile_No = int(input("Enter student Mobile number"))
        self.Mobile_No.append(Mobile_No)
        Email = input("Enter student Email")
        self.Email.append(Email)
        Password = input("Enter student Password")
        self.Password.append(Password)
        n = int(input("Enter no of modules you want to assign student"))
        a = list(map(int, input("Enter Module/Modules ID to enroll student:").strip().split()))[:n]
        self.ModuleID.append(a)

        print("---------CREATED SUCCESSFULY---------")

    def View_Student(self):
        id = int(input("Enter the contact number of student ,whose detail you want to see"))
        length = len(self.Mobile_No)
        for i in range(length):
            if (self.Mobile_No[i] == id):
                index = i
                break
        print("---------DETAILS---------")
        print("\nFull Name:", self.Full_Name[index])
        print("\nMobile Number:", self.Mobile_No[index])
        print("\nEmail:", self.Email[index])
        print("\nModule list:", self.ModuleID[index])

    def Update_Student(self):
        id = int(input("Enter the contact number of student ,whose detail you want to Update"))
        length = len(self.Mobile_No)
        for i in range(length):
            if (self.Mobile_No[i] == id):
                index = i
                break

        print("---------YOUR PREVIOS DETAILS---------")
        print("\nFull Name:", self.Full_Name[index])
        print("\nMobile Number:", self.Mobile_No[index])
        print("\nEmail:", self.Email[index])
        print("\nModule list:", self.ModuleID[index])

        print("-------------------ENTER NEW VALUES YOU WANT TO UPDATE----------------------")
        Full_Name = input("Enter student full name")
        self.Full_Name.append(Full_Name)
        Mobile_No = int(input("Enter student Mobile number"))
        self.Mobile_No.append(Mobile_No)
        Email = input("Enter student Email")
        self.Email.append(Email)
        Password = input("Enter student Password")
        self.Password.append(Password)
        n = int(input("Enter no of modules you want to assign student"))
        a = list(map(int, input("Enter Module/Modules ID to enroll student:").strip().split()))[:n]
        self.ModuleID.append(a)

    def Delete_Student(self):
        id = int(input("Enter the contact number of student ,whose detail you want to Delete"))
        length = len(self.Mobile_No)
        for i in range(length):
            if (self.Mobile_No[i] == id):
                index = i
                break
            else:
                index = -1

        if index == -1:
            print("No Record found!!!")
        else:
            del self.Full_Name[index]
            del self.Mobile_No[index]
            del self.Email[index]
            del self.ModuleID[index]
            print("Successfully deleted!!!!!")


class login(Students):

    def __init__(self):
        self.credintials = {}

    def check(self, user, pas):
        Students.__init__(self)
        length = len(self.Mobile_No)
        for i in range(length):
            if user == self.Email[i] and pas == self.Password[i]:
                return 1


obj_M = Module()
obj_S = Students()
obj_U = Unit()
while True:
    print('login \n 1-Admin \n 2-Student')
    n = int(input())
    if n == 1:
        user = input('enter email id:')
        password = input('enter password:')
        print('login success!!')
        print('choose function for operation')
        while True:
            print(' 1 Manage Modules \n 2 Manage Units \n 3 Manage Students \n 4 Logout ')
            choose_function = int(input())
            if choose_function == 1:
                print(' a:Create a new module \n b:View module details \n c:Update module \n d:Delete module ')
                choose_operations = input()
                if choose_operations == 'a':
                    obj_M.create_module()

                elif choose_operations == 'b':
                    obj_M.view_module_details()

                elif choose_operations == 'c':
                    obj_M.update_module()

                elif choose_operations == 'd':
                    obj_M.delete_module()

            elif choose_function == 2:
                print(' a:Create a new unit \n b:View all units \n c:Update unit \n d:Delete unit')
                choose_operations = input()
                if choose_operations == 'a':
                    obj_U.Create_unit()

                elif choose_operations == 'b':
                    obj_U.View_units()

                elif choose_operations == 'c':
                    obj_U.Update_unit()

                elif choose_operations == 'd':
                    obj_U.Delete_unit()

            elif choose_function == 3:
                print(' a:Create a new Student \n b:View Student details \n c:Update Student \n d:Delete Student ')
                choose_operations = input()
                if choose_operations == 'a':
                    obj_S.Create_Student()

                elif choose_operations == 'b':
                    obj_S.View_Student()

                elif choose_operations == 'c':
                    obj_S.Update_Student()

                elif choose_operations == 'd':
                    obj_S.Delete_Student()

            elif choose_function == 4:
                break

    elif n == 2:
        s = login()
        Email = (input('Please enter Email'))
        Pword = (input('Please enter password'))
        temp = s.check(Email, Pword)
        while True:
            print("Login success!")
            print(' a:View todays schedule \n b:View my module  \n c:Update profile \n d:logout ')
            choose_operations = input()
            if choose_operations == 'a':
                pass

            elif choose_operations == 'b':
                pass

            elif choose_operations == 'c':
                pass

            elif choose_operations == 'd':
                break
