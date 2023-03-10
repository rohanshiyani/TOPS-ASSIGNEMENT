stock={}
def show_manager_menu():
    print("Fruit market manager")
    print("1) Add Fruit Stock")
    print("2) View Fruit Stock")
    print("3) Update Fruit Stock")

    choice_manager=int(input("Enter Your Choice:"))
    if choice_manager==1:
        add_fruit()
        repeat()
    elif choice_manager==2:
        view_fruit()
        repeat()
    elif choice_manager==3:
        update_fruit()
    else:
        print("Invalid Choice")

def repeat():
    rc=input("Do you want to perform more operation: Press 'Y' fro yes and 'N' for no: ")
    if rc=='y' or rc=='Y':
        show_manager_menu()
    elif rc=='n' or rc=='N':
        print("********************Thanks for using*************************")

def add_fruit():
    print("ADD FRUIT STOCk")
    fruit_name=input("Enter Fruit Name:")
    fruit_qty=int(input("Enter qty (in kg):"))
    fruit_price=int(input("Enter price (For price):"))
    demo={}
    demo.update({'qty':fruit_qty,'price':fruit_price})
    stock.update({fruit_name:demo})
    

def view_fruit():
    print(stock)

def update_fruit():
    fruit_name=input("Which fruit you want to update:")
    temp=stock.get(fruit_name)
    if temp==None:
        print("not exists")
        update_fruit()
    uc=int(input("What you want to update:\n1)Price\n2)Quantity"))
    if uc==1:
        new_price=int(input("Enter new price:"))
        temp.update({'price':new_price})
        stock.update({fruit_name:temp})
        repeat()
    elif uc==2:
        new_qty=int(input("Enter New QUantity:"))
        temp.update({'Quantity':new_qty})
        stock.update({fruit_name:temp})
        repeat()
    else:
        print("invalid choice")
        repeat()            

