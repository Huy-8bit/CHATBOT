


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
from underthesea import word_tokenize
from underthesea import pos_tag

import sentence_classification


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


def get_message_process(messages_input):
    classify = sentence_classification.analysis_message(messages_input)
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


def main():
    while True:
        # print(intents)
        print("Bạn: ", end="")
        messages_input = " " + input() 
        if 'quit' in messages_input:
            break
        else:
            replay = get_message_process(messages_input)
            print("Bot: ", replay)
            

main()
            