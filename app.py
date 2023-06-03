from flask import Flask, render_template, jsonify, request
import git

app = Flask(__name__)

'kek'

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


@app.route('/update_server', methods=['POST', 'GET'])
def webhook():
    if request.method == 'POST':
        repo = git.Repo('/home/ekzoskelet/my_test_flask_app')
        origin = repo.remotes.origin
        origin.pull()

        return 'Updated PythonAnywhere successfully', 200
    else:
        return 'Wrong event type', 400


if __name__ == "__main__":
    app.run()
