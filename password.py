import time


def appendNew():
    file = open("pass\info.txt", 'a')

    print()
    print()

    userName = input("Please enter the user name: ")
    password = input("Please enter the password here: ")
    website = input("Please enter the website address here: ")

    print()
    print()

    usrnm = "UserName: " + userName + "\n"
    pwd = "Password: " + password + "\n"
    web = "Website: " + website + "\n"

    file.write("---------------------------------\n")
    file.write(usrnm)
    file.write(pwd)
    file.write(web)
    file.write("---------------------------------\n")
    file.write("\n")
    file.close

def view():
    file = open("pass\info.txt", 'r')
    print(file.read())
    time.sleep(10)
    entry = input("Would you like to add an entry?")
    if entry == "no":
        print("goodbye")
        file.close
    elif entry == "yes":
        file.close
        appendNew()
        
    


entry = input("Would you like to view an existing entry, or create a new one?")
if entry == "create":
    appendNew()
elif entry == "view":
    view()
else:
    print("Error")
