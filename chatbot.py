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
    Structure = load_data('structure.json')
    for i in range(len(Structure['subject']['self'])):
        break
        print(Structure['subject']['self'][i])
    
    
def process_message(messages_input, intents, classify):
    if classify == []:
        return "Tôi không hiểu ý bạn"
    elif 'greet' in classify:
        get_structure(messages_input)
        return "Chào bạn, tôi có thể giúp gì cho bạn"
        


intents = load_data('data.json')
classes = load_data('classify_document.json')

while True:
    # print(intents)
    print("Bạn: ", end="")
    messages_input = input()
    if messages_input == "quit":
        break
    else:
        classify = analysis_message(messages_input, classes)
        replay = process_message(messages_input, intents, classify)
        print("Bot: ", replay)