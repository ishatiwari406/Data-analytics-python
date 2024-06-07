while True:
    username=input("Enter the username:  ")
    passward=input("Enter the passward:  ")
    if username=='admin' and passward=='1234':
        print("login successful!")
        break
    else:
        print("login failed!")