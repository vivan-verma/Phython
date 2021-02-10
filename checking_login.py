#write a prgram to see if username and password are correct

username = input("Enter your username:  ")
password = input("Enter your password: ")

real_user = "python2020@gmail.com"
password2 = "SECRETpwd"

if ((username == real_user  ) and (password == password2)):
    print("Welcome", username)
else:
    print("Wrong login try again")
