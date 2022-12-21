# crate chatbot


# import logging
import os
import sys
import os.path
import math
import os
import re
import numpy as np
import random
import json
import nltk
# nltk.download('punkt')
# nltk.download('stopwords')
# nltk.download('wordnet')
from underthesea import word_tokenize
from underthesea import pos_tag

# import data.json


def load_data(file_path):
    with open(file_path, encoding="utf8") as json_data:
        intents = json.load(json_data)

    return intents


def preprocess_message(documents):
    # convert to array of token
    list_results = documents.split()
    for i in range(len(list_results)):
        list_results[i] = list_results[i].lower()
    return list_results


def analysis_message(messages_input, classes):
    classify = []
    for i in range(len(classes['intents'])):
        for j in range(len(classes['intents'][i]['key'])):
            check = messages_input.find(classes['intents'][i]['key'][j])
            if check > 0:
                text = classes['intents'][i]['type']
                classify.append(text)

    return classify


def get_structure(messages_input):
    result = pos_tag(messages_input)
    return result


def process_message(messages_input):
    structure = get_structure(messages_input)


def find_classify_key(structure, key_classify):
    for i in range(len(structure)):
        if structure[i][1] == key_classify:
            return structure[i][0]
    return ""


def process_message_question(messages_input):
    print("process_message_question")
    structure = get_structure(messages_input)
    print(word_tokenize(messages_input))
    print("structure: ", structure)
    check_key = find_classify_key(structure, "E")


def get_message_process(messages_input):
    classify = analysis_message(messages_input, classes)
    print("classify: ", classify)
    if 'question' in classify:
        process_message_question(messages_input)
        return "tôi sẽ tìm câu trả lời cho bạn"
    elif 'greet' in classify:
        process_message(messages_input)
        return "Chào bạn, tôi có thể giúp gì cho bạn"
    elif 'request' in classify:
        process_message(messages_input)
        return "Bạn muốn tôi giúp gì cho bạn?"

    elif 'exclamatory' in classify:
        process_message(messages_input)
        return "Tôi rất vui vì được giúp đỡ bạn"
    else:
        return "Tôi không hiểu bạn nói gì"


classes = load_data('classify_document.json')

while True:
    # print(intents)
    print("Bạn: ", end="")
    messages_input = " " + input()
    if messages_input == " quit":
        break
    else:
        replay = get_message_process(messages_input)
        print("Bot: ", replay)
