from flask import Flask

app = Flask(__name__)


# first endpoint #
@app.route('/')
def hello_world():
    return 'Flask Dockerized - 21'



if __name__ == '__main__':
    # Changes done by Hardik Starts
    print("Changes done by Hardik with Akash_Docker_Branch_2")
    # Changes done by Hardik Ends

    app.run(debug=False, host='127.0.0.1', port=5020)
