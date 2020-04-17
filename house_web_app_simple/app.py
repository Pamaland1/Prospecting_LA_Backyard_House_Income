from flask import Flask, request, render_template
from make_prediction import backyard_house


# create a flask object
app = Flask(__name__)

# creates an association between the / page and the entry_page function (defaults to GET)
@app.route('/')
def entry_page():
    return render_template('index.html')

# creates an association between the /predict_recipe page and the render_message function
# (includes POST requests which allow users to enter in data via form)
@app.route('/predict_income/', methods=['GET', 'POST'])
def render_message():

    final_message = backyard_house(request.form['address'])
    return render_template('index.html', message=final_message)

if __name__ == '__main__':
    app.run(debug=True)
