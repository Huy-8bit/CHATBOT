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
    result = word_tokenize(messages_input)
    print(result)
    

def process_message(messages_input):
    structure = get_structure(messages_input)
    
    
        
    
def get_message_process(messages_input, intents):
    classify = analysis_message(messages_input, classes)
    if 'greet' in classify:
        process_message(messages_input)
        return "Chào bạn, tôi có thể giúp gì cho bạn"
    elif 'request' in classify:
        process_message(messages_input)
        return "Bạn muốn tôi giúp gì cho bạn?"
    elif 'question' in classify:
        process_message(messages_input)
        return "tôi sẽ tìm câu trả lời cho bạn"
    elif 'exclamatory' in classify:
        process_message(messages_input)
        return "Tôi rất vui vì được giúp đỡ bạn"
    else:
        return "Tôi không hiểu bạn nói gì"

intents = load_data('data.json')
classes = load_data('classify_document.json')

while True:
    # print(intents)
    print("Bạn: ", end="")
    messages_input = " " + input()
    if messages_input == " quit":
        break
    else:
        replay = get_message_process(messages_input, intents)
        print("Bot: ", replay)
    
  