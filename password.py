def password_check(password, code):
    while len(password) >= 8 and len(password) < 64:
        print("Good Length")
        code = input("Password Check: ")
        while code != password:
              code = input('Please check the password: ')
        print("Password Checked")
    print ("Password need more caracteres")

print("Password: ")
password = input()
code = ""
password_check(password, code)
