def login():
  while True:
    user = input("Enter your username: ")
    password = input("Enter your password: ")
    if user == "user" and password == "password":
      print("Welcome, User!")
      break
    else:
      print("")
      continue
print("Login")
login()