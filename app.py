from flask import Flask, render_template, jsonify, request
import git

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


@app.route('/update_server')
def webhook():
    repo = git.Repo('./my_test_flask_app')
    for remote in repo.remotes:
        remote.fetch()
    repo.git.reset('--hard', 'origin/master')
    return 'Updated PythonAnywhere successfully', 200


if __name__ == "__main__":
    app.run()
