# app.py

from flask import Flask, render_template, request, jsonify
from pwcheck import regex_check, zxcvbn_check

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def password_check():
    result = None
    if request.method == 'POST':
        password = request.form['password']
        
        # Check using regex
        regex_result = regex_check(password)
        print("Regex Result:", regex_result)  # Debugging line
        
        # Check using zxcvbn
        zxcvbn_result = zxcvbn_check(password)
        
        result = {
            'regex_result': regex_result,
            'strength_score': zxcvbn_result['strength_score'],
            'feedback': zxcvbn_result['feedback']
        }
    return render_template('index.html', result=result)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
