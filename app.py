from flask import Flask, render_template
import json

app = Flask(__name__)


@app.route("/", methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/fetchtest', methods=['GET'])
def fetchtest():
    f = open('db.json')
    data = json.load(f)
    return data


if __name__ == '__main__':
    app.run(debug=True, port=5000)
