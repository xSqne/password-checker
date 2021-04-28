import os

from flask import Flask, render_template, request

app = Flask(__name__, template_folder='templates')


def pswdcheck(a):
    criterion = False
    strength = 0

    while not criterion:
        pswd = [x for x in a]

        if len(pswd) < 6 or len(pswd) > 12:
            return "The password must be at least 6 and no more than 12 characters long"

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

            return "Password accepted.\nPassword Strength: " + strength


@app.route('/form')
def form():
    return render_template('form.html')


@app.route('/data/', methods=['POST', 'GET'])
def data():
    if request.method == 'GET':
        return f"The URL /data is accessed directly. Try going to '/form' to submit form"
    if request.method == 'POST':
        form_data = request.form

        for key, value in form_data.items():
            a = value
            result = pswdcheck(a)
            return render_template('data.html', result=result)


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)