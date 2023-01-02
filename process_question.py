from underthesea import word_tokenize
from underthesea import pos_tag

import re

import sentence_classification


def get_structure(messages_input):
    result = word_tokenize(messages_input)
    return result
         
def check_story(messages_input, classify):
    print("Checking story")
    data = sentence_classification.load_data('story.json')
    for value in data['data']:
        if classify in value['tag']:
            for result in value['story']:
                if messages_input in result['patterns']:
                    return result['responses'][0]
    print("Not found in story")
    return "NULL"


def get_important_key(messages_input,data):
    print("")
    print("Getting important key")
    stuct_message = get_structure(messages_input)
    print("struct: ", stuct_message)
    print("")
    classes = "NULL"
    for value in data['classes']:
        print(value['key']) 
        if classes in value['key']:
            classes = value['classes']
            break
            
    print("classes: ", classes)

def process_message_question(messages_input, data):
    # Get the answer to the question
    print("")
    print("Processing question")
    get_important_key(messages_input, data)
    return "Chưa biết trả lời câu hỏi này!!!"    





def test():
    messages_input = "tôi muốn hỏi về địa chỉ của ngân hàng vietcombank?"
    # messages_input = "khi nào mở cửa ngân hàng?"
    print("messages_input: ", messages_input)
    classify = sentence_classification.analysis_message(messages_input)
    print("classify: ", classify[0])
    print("")
    result = check_story(messages_input, classify[0])
    if result == "NULL":
        data = sentence_classification.load_data('question.json')
        result = process_message_question(messages_input, data)
        
    print("bot: ", result)
    


    
test()

