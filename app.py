from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['GET', 'POST'])
def calculate_paycheck():
    if request.method == 'POST':
        try:
            user_paycheck = float(request.form['pay_amount'])
            user_hours = float(request.form['hours_worked'])
            hours_limit = 40

            total_calculated = user_hours * user_paycheck

            if user_hours <= hours_limit:
                result = f'Your total paycheck is $ {total_calculated:.2f}'
            else:
                result = 'Invalid hours'

            return render_template('results.html', result=result)
        except ValueError:
            result = 'Invalid input. Please enter valid numbers.'
            return render_template('results.html', result=result)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
