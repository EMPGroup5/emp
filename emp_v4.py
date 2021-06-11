import datetime
import json

# list of all saved employees
employees = []


def print_choose():
    print("Please choose one of the following options:")


def print_not_developed():
    print("This function is not developed yet.")


def print_not_valid():
    print("This is not a valid option!")


def choose_between(start, end):
    print("Please enter a number between", start, "and", str(end) + "!")
    return input("Input: ")


def create_menu():
    while True:

        print_choose()
        print("1. add datasets from file (merge)\n2. add new single dataset (via console)\n"
              "3. add new column (for all datasets)\n4. back")
        selection = choose_between(1, 4)
        if selection == "1":
            print_not_developed()
        elif selection == "2":
            add_employee()
            with open('database.json', 'w', encoding='utf-8') as f:
                json.dump(employees, f, ensure_ascii=True, indent=4)
        elif selection == "3":
            print_not_developed()
        elif selection == "4":
            break
        else:
            print_not_valid()


def add_employee():
    # Instructions output
    print("Please add the employee data!")
    employee = {"id": int(input("ID: ")), "firstname": input("Firstname: "), "lastname": input("Lastname: "),
                "date_of_birth": input("Date of birth (dd.mm.yyyy): "),
                "address": input("Address: "), "department": input("Department: "),
                "phone_number": input("Phone number: "), "employment_status": input("Employment status: "),
                "gender": input("Gender: "), "drivers_license": input("Driver's license: "),
                "religion": input("Religion: "), "health_insurance": input("Health Insurance: "),
                "marital_status": input("Marital status: "), "salary": float(input("Salary in euros: ")),
                "email": input("E-mail address: "), "superior": input("Superior: "),
                "entry_date": input("Date of entry (dd.mm.yyyy): ")}
    employees.append(employee)

    # Confirmation
    print()
    print("The employee", employee["firstname"], employee["lastname"], "was added successfully.\n")


def read_menu():
    while True:
        print_choose()
        print("1. show all datasets\n2. show single dataset\n3. filter ...\n"
              "4. show empty fields\n5. back")
        selection = choose_between(1, 5)
        if selection == "1":
            print_all()
        elif selection == "2":
            print_not_developed()
        elif selection == "3":
            print_not_developed()
        elif selection == "4":
            print_not_developed()
        elif selection == "5":
            break
        else:
            print_not_valid()


def print_all():
    f = open("database.json", "r", encoding="utf-8")
    a_employees = json.load(f)
    f.close()
    counter = 1
    for employee in a_employees:
        print("Employee #", counter)
        print("The employee's ID:", employee["id"])
        print("The employee's Firstname:", employee["firstname"])
        print("The employee's Lastname:", employee["lastname"])
        import_birthday = employee["date_of_birth"]
        birthday = datetime.datetime.strptime(import_birthday, '%d.%m.%Y')
        print("The employee's Age:", round(abs((datetime.datetime.today() - birthday).days / 365)))
        print("The employee's Address:", employee["address"])
        print("The employee's Department:", employee["department"])
        print("The employee's Phone number:", employee["phone_number"])
        print("The employee's employment status:", employee["employment_status"])
        print("The employee's gender:", employee["gender"])
        print("The employee's driver's License(s):", employee["drivers_license"])
        print("The employee's religion:", employee["religion"])
        print("The employee's health insurance:", employee["health_insurance"])
        print("The employee's marital status:", employee["marital_status"])
        print("The employee's salary:", employee["salary"])
        print("The employee's e-mail address:", employee["email"])
        print("The employee's superior:", employee["superior"])
        print("The employee's entry date:", employee["entry_date"])
        print("\n")
        counter += 1


def update_menu():
    while True:
        print_choose()
        print("1. update all\n2. update single dataset\n3. back")
        selection = choose_between(1, 3)
        if selection == "1":
            print_not_developed()
        elif selection == "2":
            print_not_developed()
        elif selection == "3":
            break
        else:
            print_not_valid()


def delete_menu():
    while True:
        print_choose()
        print("1. delete all\n2. delete single row\n3. delete single column\n4. back")
        selection = choose_between(1, 4)
        if selection == "1":
            print_not_developed()
        elif selection == "2":
            print_not_developed()
        elif selection == "3":
            print_not_developed()
        elif selection == "4":
            break
        else:
            print_not_valid()


def main_menu():
    print("Welcome to the Employee Management Program (EMP)\n==================================================")
    while True:
        print_choose()
        print("1. create\n2. read\n3. update\n4. delete\n5. save/export\n6. end program")
        selection = choose_between(1, 6)
        if selection == "1":
            create_menu()
        elif selection == "2":
            read_menu()
        elif selection == "3":
            update_menu()
        elif selection == "4":
            delete_menu()
        elif selection == "5":
            print_not_developed()
        elif selection == "6":
            print("Good Bye!\n====================== END =======================")
            break
        else:
            print_not_valid()


if __name__ == '__main__':
    main_menu()
