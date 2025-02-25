from prettytable import PrettyTable

# Global list to store user data
ids_list = []

# Function to sign up users
def sign_up(name, email, password):
    ids = {"NAME": name, "EMAIL": email, "PASSWORD": password}
    ids_list.append(ids)
    print(f"User {name} registered successfully!")

# Function to log in users
def login(name, email, password):
    for i in ids_list:
        if i["NAME"] == name and i["EMAIL"] == email and i["PASSWORD"] == password:
            print("LOGIN SUCCESSFUL")
            return True
        if i["NAME"] != name and i["EMAIL"] == email and i["PASSWORD"] == password:
            print("INCORRECT NAME")
        if i["NAME"] == name and i["EMAIL"] != email and i["PASSWORD"] == password:
            print("INCORRECT EMAIL")
        if i["NAME"] == name and i["EMAIL"] == email and i["PASSWORD"] != password:
            print("INCORRECT PASSWORD")
            return False

# Function to display all users
def display_user():
    if not ids_list:
        print("No one has registered.")
        return
    
    table = PrettyTable()
    table.field_names = ["NAME", "EMAIL", "PASSWORD"]
    
    for k in ids_list:
        table.add_row([k["NAME"], k["EMAIL"], k["PASSWORD"]])
    
    print(table)

# Function to delete a user by email
def delete_user(email):
    for k in ids_list:
        if k["EMAIL"] == email:
            ids_list.remove(k)
            print(f"User with name {k['NAME']} email {email} deleted successfully!")
            return
    print("User not found")

# Testing the functions
sign_up("Alice", "alice@example.com", "pass123")
sign_up("Bob", "bob@example.com", "pass456")
sign_up("ustad","ustadi@example.com","12345679")
login("Alice", "alice@example.com", "pass123")  # Pass
login("Bob", "bob@example.com", "wrongpass")    # Fail

display_user()

delete_user("alice@example.com")
display_user()
