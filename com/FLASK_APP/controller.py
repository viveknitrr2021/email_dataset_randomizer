from flask import Flask

app = Flask(__name__)

@app.route('/health', methods=['GET', 'POST'])
def welcome():
    return "Health Check Successful"


if __name__ == '__main__':
    app.run()