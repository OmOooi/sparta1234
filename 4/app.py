from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    user_choice = None
    computer_choice = None

    if request.method == 'POST':
        user_choice = request.form['user_choice']
        computer_choice = random.choice(['가위', '바위', '보'])
        result = determine_winner(user_choice, computer_choice)

    return render_template('index.html', result=result, user_choice=user_choice, computer_choice=computer_choice)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return '무승부'
    elif (
        (user_choice == '가위' and computer_choice == '보') or
        (user_choice == '바위' and computer_choice == '가위') or
        (user_choice == '보' and computer_choice == '바위')
    ):
        return '이겼습니다!'
    else:
        return '졌습니다.'

if __name__ == '__main__':
    app.run(debug=True)