import manager
import customer
def start():
    print("welcome to fruit market:")
    print("1) manager")
    print("2) customer")

    role=int(input("enter your role:"))

    if role==1:
        manager.show_manager_menu()
    elif role==2:
        pass
    else:
        print("Invalid role")
start()

