from underthesea import word_tokenize
from underthesea import pos_tag

import re

import sentence_classification


def get_structure(messages_input):
    result = word_tokenize(messages_input)
    return result




def find_responses(messages_input, data):
    key = []
    response = []
    subject = []
    for value in data[0]:
        if value['subject'] in messages_input:
            subject = value['subject']
            for keys in value['key']:
                if keys in messages_input:
                    key.append(keys)
                    index = value['key'].index(keys)
                    response.append(value['responses'][index])
    return response, key, subject


def build_answer(messages_input, data, classes, type):
    messages = get_structure(messages_input)
    new_data = []
    response, key, subject = [], [], []
    answer = ""
    for value in data['table']:
        if classes in value['classes']:
            new_data.append(value['data'])
            response, key, subject = find_responses(messages_input, new_data)
            if response != [] and key != []:    
                for i in range(0, len(response) - 1):
                    answer += key[i] + " của " + subject + " là " + response[i] + ", "
                answer += key[len(response) - 1] + " của " + subject + " là " + response[len(response) - 1]
                return answer
    answer = "Tôi chưa hiểu đúng câu hỏi của bạn :< "
    return answer


def get_important_key(messages_input, data):
    stuct_message = get_structure(messages_input)
    classes = "NULL"
    type = "NULL"
    for word in stuct_message:
        for value in data['classes']:
            if word in value['key']:
                classes = value['classes'][0]
                break
        for value in data['quection']:
            if word in value['key']:
                type = value['type'][0]
                break

    return classes, type


def process_message_question(messages_input, data):
    # Get the answer to the question

    classes, type = get_important_key(messages_input, data)
    if classes != "NULL" or type != "NULL":

        result = build_answer(messages_input, data, classes, type)
        return result
    else:
        return "Chưa biết trả lời câu hỏi này!!!"


def question(messages_input):
    messages_input = messages_input.lower()
    data = sentence_classification.load_data('question.json')
    result = process_message_question(messages_input, data)
    return result
