import requests

import main
import sentence_classification
import process_question
import check_story
from flask import *
app = Flask(__name__)

chatbotStories = [{'patterns': "khi nào mở cửa ngân hàng?",'responses': "ngân hàng mở cửa từ 8h sáng đến 17h chiều từ thứ 2 đến thứ 6. ngân hàng đóng cửa vào thứ 7 và chủ nhật."}]

#Homepage
@app.route('/',methods =['GET'])
def homepage():
    dataSet = {'Page':'Homepage', 'Message':'Welcome to my Chatbot'}
    json_data = json.dumps(dataSet)
    return json_data

#Get all stories
@app.route('/getAllStories',methods =['GET'])
def stories():
    dataSet = {'Page':'Stories', 'Message':'All stories'}
    json_data = json.dumps(dataSet)
    return json_data

#Add question to story
@app.route('/chatbot',methods =['POST'])
def chatbot():
    chatbotStory = {'patterns': request.json['patterns'],'responses': request.json['responses']}
    chatbotStories.append(chatbotStory)
    return jsonify({'chatbotStories' : chatbotStories})

#Put question
#Đang lỗi URL vì truyền pattern vào không nhận khoảng cách
@app.route('/chatbotedit/<string:patterns>',methods =['PUT'])
def editQues(patterns):
    editQues = [chatbotStory for chatbotStory in chatbotStories if chatbotStory['patterns'] == patterns]
    editQues[0]['patterns'] = request.json['patterns']
    return jsonify({'chatbotStories': editQues[0]})


#Delete question
#Lỗi out of range
@app.route('/chatbot/<string:patterns>',methods =['DELETE'])
def removeQues(patterns):
    deleteQues = [chatbotStory for chatbotStory in chatbotStories if chatbotStory['patterns'] == patterns]
    chatbotStories.remove(deleteQues[0])
    return jsonify({'chatbotStories': chatbotStories})

if __name__ == '__main__':
    app.run(port=7777)
