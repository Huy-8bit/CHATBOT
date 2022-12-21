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


def get_struct():


def find_classify_key(structure, key_classify):
    for i in range(len(structure)):
        if structure[i][1] == key_classify:
            return structure[i][0]
    return ""


def process_message_question():
    print("process_message_question")


def get_message_process():
    classify = 'question'
    if classify == 'question':
        process_message_question("")
