# This is the actual script that can be ran using 'python script.py'

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

        # Checking if there are any numerals
        for item in pswd:
            if item.isnumeric():
                strength += 1
                break

        # Check if there are any special characters
        for item in pswd:
            if item.isalnum():
                strength += 1
                break

        if strength == 0:
            strength = "Weak"
        elif strength == 1:
            strength = "Medium"
        elif strength == 2:
            strength = "Strong"
        elif strength == 3:
            strength = "OVERPOWERED"

        print("Password accepted.\nPassword Strength:", strength)
        strength = 0
