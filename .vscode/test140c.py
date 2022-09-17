again = "y"
while again == "y":
        print()
        print("Main Menu")
        print()
        print("1) View phone book")
        print("2) Add to phone book")
        print("3) Search for surname")
        print("4) Delete person from phone book")
        print("5) Quit")
        print()
        
        #selection = int(input("Enter your selection: "))               
        selection = 5
        print("selection  = ", selection)
if selection == 1:
        print("1")
elif selection == 2:
        print("2")
elif selection == 3:
        print("3")
elif selection == 4:
        print("4")
elif selection ==5:
        again = "n"
else:
        print("Incorrect selection entered")