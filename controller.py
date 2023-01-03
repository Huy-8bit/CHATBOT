import process_question
from flask import *
app = Flask(__name__)

@app.route('/',methods =['GET'])
def homepage():
    dataSet = {'Page':'Homepage', 'Message':'Welcome to my Chatbot'}
    json_data = json.dumps(dataSet)
    return json_data


if __name__ == '__main__':
    app.run(port=7777)
