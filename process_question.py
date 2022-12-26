from underthesea import word_tokenize
from underthesea import pos_tag

import re

import sentence_classification


def get_structure(messages_input):
    result = word_tokenize(messages_input)
    return result









def get_important_key(messages_input,data):
    list_key = word_tokenize(messages_input)
    classes = ""
    key = ""
    for key in list_key:
        for value in data['classes']:
            if key in value['key']:
                classes = value['classes']
                key = key
    type = ""
    for key in list_key:
        for value in data['quection']:
            if key in value['key']:
                type = value['type']
    return classes, key, type            


def get_response(classes, key, type, data):
    response = "NULL"
    # for value in data['data']:
    #     print(value['patterns'])
    return response


def get_answer( classes, key, type, data):
    return get_response(classes, key, type, data)



def check_story(messages_input, classify):
    print("Checking story")
    
    
    data = sentence_classification.load_data('story.json')
    for value in data['data']:
        if classify in value['tag']:
            for result in value['story']:
                if messages_input in result['patterns']:
                    return result['responses'][0]
        else:
            print("Don't have this story")
    return "NULL"

def process_message_question(messages_input, data):
    # Get the answer to the question
    
    classes, key, type = get_important_key(messages_input, data)
    response = get_response(classes, key, type, data)
    answer = get_answer(classes, key, type, data)
    return answer




def test():
    messages_input = "tôi muốn hỏi về địa điểm của ngân hàng?"
    
    print("messages_input: ", messages_input)
    classify = sentence_classification.analysis_message(messages_input)
    print("classify: ", classify[0])
    result = check_story(messages_input, classify[0])
    if result == "NULL":
        data = sentence_classification.load_data('question.json')
        result = process_message_question(messages_input, data)
    print("bot: ", result)
    


    
test()

