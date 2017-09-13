from flask import Flask, render_template, redirect, session

app = Flask (__name__)

@app.route ('/')
def index():
    return render_template('index.html')


@app.route('/result', methods=['POST'])
def result():
    # print request.form
    return render_template ('result.html',data=data)

app.run(debug=True)