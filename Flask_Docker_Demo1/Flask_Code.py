from flask import Flask

app = Flask(__name__)


# first endpoint #
@app.route('/')
def hello_world():
    return 'Flask Dockerized - 11'


if __name__ == '__main__':
    app.run(debug=False, host='127.0.0.1', port=5010)
    # Adding comments for Branch 4
