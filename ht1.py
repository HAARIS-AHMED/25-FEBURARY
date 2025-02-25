from prettytable import PrettyTable

ids_list = []

def sign_up(name, email, password):
    for k in ids_list:
        if k["EMAIL"] == email:
            print("This email is already registered!")
            return
    ids = {"NAME": name, "EMAIL": email, "PASSWORD": password}
    ids_list.append(ids)
    print(f"{name} signed up successfully")

def login(name, email, password):
    for k in ids_list:
        if k["NAME"] == name and k["EMAIL"] == email and k["PASSWORD"] == password:
            print("LOGIN SUCCESSFUL")
            return True
        elif k["EMAIL"] == email and k["PASSWORD"] == password:
            print("INCORRECT NAME")
            return False
        elif k["NAME"] == name and k["PASSWORD"] == password:
            print("INCORRECT EMAIL")
            return False
        elif k["NAME"] == name and k["EMAIL"] == email:
            print("INCORRECT PASSWORD")
            return False
    print("USER NOT FOUND")
    return False

def display_user():
    if not ids_list:
        print("No one has registered.")
        return
    
    table = PrettyTable()
    table.field_names = ["NAME", "EMAIL", "PASSWORD"]
    
    for k in ids_list:
        table.add_row([k["NAME"], k["EMAIL"], k["PASSWORD"]])
    
    print(table)

def delete(email, password):
    for k in ids_list:
        if k["EMAIL"] == email and k["PASSWORD"] == password:
            ids_list.remove(k)
            print(f"{k['NAME']} successfully deleted.")
            return
    print("USER NOT FOUND")

# Menu-driven program
while True:
    print("\n1. Sign Up")
    print("2. Login")
    print("3. Display Users")
    print("4. Delete User")
    print("5. Exit")
    
    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter name: ")
        email = input("Enter email: ")
        password = input("Enter password: ")
        sign_up(name, email, password)
    
    elif choice == "2":
        name = input("Enter name: ")
        email = input("Enter email: ")
        password = input("Enter password: ")
        login(name, email, password)
    
    elif choice == "3":
        display_user()
    
    elif choice == "4":
        email = input("Enter email to delete: ")
        password = input("Enter password: ")
        delete(email, password)
    
    elif choice == "5":
        print("Exiting...")
        break
    
    else:
        print("Invalid choice. Please try again.")
