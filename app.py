from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

'blyat try'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contacts')
def contacts():
    return render_template('contacts.html')


@app.route('/api')
def api():
    return jsonify({"message": "Hello pes!"})


if __name__ == "__main__":
    app.run()
