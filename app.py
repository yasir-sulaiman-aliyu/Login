def login():
    print("*********Welcome to Yastech*******")
    while True:
        name = input("Enter your fullname:" + " ")
        password = input("Enter your password:" + " ")
        correct_password = "Yastech"
        if password == correct_password:
            print("Welcome to Yastech" + " " + name)
            break
        else:
            print("Invalide Login, try again")
            print("-"*30)


login()
