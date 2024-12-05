print("You are taking a test only above 13 years can enter")
try:
    age=int(input("Enter your age: "))
    if (age<13):
        raise ValueError
    else:
        print("Age is valid You are allowed to take the test :)")

except ValueError:
    print("Age is invalid Sorry You can not attend the test :(")