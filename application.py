from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/terms-and-conditions')
def terms():
    return render_template('terms-conditions.html', title='Terms and Conditions')


@app.route('/privacy-policy')
def privacy():
    return render_template('privacy-policy.html', title='Privacy Policy')