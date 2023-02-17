from flask import Flask, render_template
import json

app = Flask(__name__)


@app.route('/<title1>')
@app.route('/index/<title1>')
def index(title1):
    return render_template('index.html', title=title1)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
