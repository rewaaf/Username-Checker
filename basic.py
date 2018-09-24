from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit')
def result():
    username = request.args.get('username')
    upper = False
    lower = False
    num_end = False
    for item in username: #must search for whole string
        if item.isupper():
            upper = True
        if item.islower():
            lower = True
    if item[-1].isdigit(): #doesn't require search just check last digit
        num_end = True
    if upper and lower and num_end:
        end_result = True
    else:
        end_result = False
    return render_template('submit.html',end_result=end_result,upper=upper,lower=lower,num_end=num_end)

if __name__ == '__main__':
    app.run(debug=True)
