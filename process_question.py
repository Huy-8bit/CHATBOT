from underthesea import word_tokenize
from underthesea import pos_tag

import re

import sentence_classification


def get_structure(messages_input):
    result = word_tokenize(messages_input)
    return result


def check_story(messages_input, classify):
    data = sentence_classification.load_data('story.json')
    for value in data['data']:
        if classify in value['tag']:
            for result in value['story']:
                if messages_input in result['patterns']:
                    return result['responses'][0]
    print("Not found in story")
    return "NULL"


def find_responses(messages_input, data):
    print("Finding responses")
    key = []
    response = []
    subject = []
    for value in data[0]:
        if value['subject'] in messages_input:
            print("value: ", value)
            for keys in value['key']:
                if keys in messages_input:
                    key.append(keys)
                    index = value['key'].index(keys)
                    response.append(value['responses'][index])
                    subject = value['subject']
    return response, key, subject


def build_answer(messages_input, data, classes, type):
    print("Building answer")
    messages = get_structure(messages_input)
    new_data = []
    response, key, subject = [], [], []
    answer = "chưa hiểu câu hỏi của bạn!"
    for value in data['table']:
        if classes in value['classes']:
            new_data.append(value['data'])
            response, key, subject = find_responses(messages_input, new_data)
            answer = ""
            for i in range(0, len(response) - 1):
                answer += key[i] + " của " + subject + \
                    " là " + response[i] + ", "
            answer += key[len(response) - 1] + " của " + \
                subject + " là " + response[len(response) - 1]
            return answer

    return answer


def get_important_key(messages_input, data):
    print("")
    print("Getting important key")
    stuct_message = get_structure(messages_input)
    print("struct: ", stuct_message)
    print("")
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
    print("")
    print("Processing question")
    classes, type = get_important_key(messages_input, data)
    if classes != "NULL" or type != "NULL":

        result = build_answer(messages_input, data, classes, type)
        return result
    else:
        return "Chưa biết trả lời câu hỏi này!!!"


def test():
    messages_input = input("user: ")
    messages_input = messages_input.lower()
    # messages_input = "khi nào mở cửa ngân hàng?"
    print("messages_input: ", messages_input)
    classify = sentence_classification.analysis_message(messages_input)
    print("classify: ", classify[0])
    print("")
    result = check_story(messages_input, classify[0])
    if result == "NULL":
        data = sentence_classification.load_data('question.json')
        result = process_message_question(messages_input, data)
    print("")
    print("bot: ", result)


test()
