from flask import Flask
from com.DBAI.datasetgenerator import generate_dataset


app = Flask(__name__)

@app.route('/health', methods=['GET', 'POST'])
def welcome():
    return "Health Check Successful"

@app.route('/createdataset', methods=['GET', 'POST'])
def create_dataset():
    # generate_dataset()
    return "dataset created"

if __name__ == '__main__':
    app.run()