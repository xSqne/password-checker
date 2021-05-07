import os
from flask import Flask, render_template, request

app = Flask(__name__, template_folder='templates')


# Function to check common passwords from file
def checkfile(x):
    # Password file forked from https://github.com/danielmiessler/SecLists/blob/master/Passwords/Common-Credentials/10k-most-common.txt
    with open("10k-most-common.txt", 'r') as file:
        for line in file:
            if x in line:
                return True

    return False


# From script.py
def pswdcheck(a):
    special_characters = "\"\'!@ #$%^&*()-+?_=,<>/"
    strength = 0
    allnumber = True

    # Check right away to reduce time
    if checkfile(a):
        return "Password found in common password database. Please change ASAP!"

    # Convert string into list
    pswd = [x for x in a]

    # 6 < Password Length < 12
    if len(pswd) < 6 or len(pswd) > 12:
        return "The password must be at least 6 and no more than 12 characters long"

    # Check if all lower or upper or contains only numbers
    if not(a.islower() or a.isupper()):
        if not(a.isnumeric()):
            strength += 1

    # Check if password is all numeral
    if not(a.isnumeric()):
        allnumber = False
    elif a.isnumeric:
        allnumber = True

    if not allnumber:
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

    # Assign values
    if strength == 0:
        strength = "Weak"
    elif strength == 1:
        strength = "Medium"
    elif strength == 2:
        strength = "Strong"
    elif strength == 3:
        strength = "OVERPOWERED"

    return "Password accepted.\nPassword Strength: " + str(strength)


# / directory
@app.route('/')
def form():
    return render_template('form.html')


# /data directory
@app.route('/data', methods=['POST', 'GET'])
def data():
    # someone might access it directly with a GET request
    if request.method == 'GET':
        return f"Trying to test my website eh? It's foolproof"

    # receiving POST request from form.html
    if request.method == 'POST':
        form_data = request.form

        for key, value in form_data.items():
            a = value
            result = pswdcheck(a)
            return render_template('data.html', result=result)


if __name__ == "__main__":
    # Tries to retrieve the port from Heroku
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
