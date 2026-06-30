from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return render_template('index.html')


@app.route('/enviar', methods=['POST'])
def enviar():  # put application's code here
    return render_template('index.html')


@app.route("/status")
def status():
    return "ON"


if __name__ == '__main__':
    app.run()
