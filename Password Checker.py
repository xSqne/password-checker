criterion = False
strength = 0

while not criterion:
    a = input("---------------------------------------\nEnter your password: ")

    if a.lower() == "stop" or a.lower() == "exit":
        exit()

    pswd = [x for x in a]

    if len(pswd) < 6 or len(pswd) > 12:
        print("The password must be at least 6 and no more than 12 characters long")

    else:
        if a.islower() or a.isupper():
            pass
        else:
            strength += 1

        for item in pswd:
            if item.isnumeric():
                strength += 1
                break

        if strength == 0:
            strength = "Weak"
        elif strength == 1:
            strength = "Medium"
        elif strength == 2:
            strength = "Strong"

        print("Password accepted.\nPassword Strength:", strength)
        strength = 0
