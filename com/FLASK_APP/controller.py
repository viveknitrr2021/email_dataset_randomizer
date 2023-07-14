from flask import Flask
from app import predict

app = Flask(__name__)

@app.route('/health', methods=['GET', 'POST'])
def welcome():
    return "Health Check Successful"

@app.route('/check', methods=['GET', 'POST'])
def check():
    return predict("Confirmation Details Trade affirmation Summary Report Trade Confirmation Affirmation of 8991889924 LVL see the following attachment Affirmation statement.json")

if __name__ == '__main__':
    app.run()

