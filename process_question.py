from underthesea import word_tokenize
from underthesea import pos_tag

import re

import sentence_classification


def get_structure(messages_input):
    result = word_tokenize(messages_input)
    return result





def get_answer(messages_input, data):
    # Get the structure of the message
    print(data)
    return "NULL"




def process_message_question(messages_input, data):
    # Get the answer to the question
    answer = get_answer(messages_input, data)
    return answer


def check_data(data):
    message = "Tôi muốn hỏi khi nào bắt đầu mở cửa ngân hàng?"
        

def test():
    messages_input = "Tôi muốn hỏi khi nào bắt đầu mở cửa ngân hàng?"
    
    print("messages_input: ", messages_input)
    classify = sentence_classification.analysis_message(messages_input)
    print("classify: ", classify[0])
    data = sentence_classification.load_data('question.json')
    # result = process_message_question(messages_input, data)
    check_data(data)
    # print("result: ", result)
    
    


    
test()


