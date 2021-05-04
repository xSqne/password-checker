# This is the actual script that can be ran using 'python script.py'

criterion = False
strength = 0
special_characters = "\"\'!@ #$%^&*()-+?_=,<>/"


# Function to check common passwords from file
def checkfile(x):
    # Password file forked from https://github.com/danielmiessler/SecLists/blob/master/Passwords/Common-Credentials/10k-most-common.txt
    with open("10k-most-common.txt", 'r') as file:
        for line in file:
            if x in line:
                return True

    return False


while not criterion:
    a = input("---------------------------------------\nEnter your password: ")

    # Exit program if input is stop/exit
    if a.lower() == "stop" or a.lower() == "exit":
        exit()

    # Check right away to reduce time
    if checkfile(a):
        print("Password found in common password database. Please change ASAP!")
        break

    # Convert string into list
    pswd = [x for x in a]

    # Check 6 < password < 12
    if len(pswd) < 6 or len(pswd) > 12:
        print("The password must be at least 6 and no more than 12 characters long")

    else:
        # Check if all upper or lower
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
                if item in special_characters:
                    strength += 1
                    break

            # Assign value
            if strength == 0:
                strength = "Weak"
            elif strength == 1:
                strength = "Medium"
            elif strength == 2:
                strength = "Strong"
            elif strength == 3:
                strength = "OVERPOWERED"

            print("Password accepted.\nPassword Strength: " + str(strength))
