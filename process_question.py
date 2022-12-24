from underthesea import word_tokenize
from underthesea import pos_tag

import re

import sentence_classification


def get_structure(messages_input):
    result = word_tokenize(messages_input)
    return result

def find_classify_key(structure, key_classify):
    for i in range(len(structure)):
        if structure[i][1] == key_classify:
            return structure[i][0]
    return ""



def get_answer(messages_input, data):
    # Tokenize the input message
    structure = get_structure(messages_input)
    # Convert the tokens to lowercase
    lower_structure = [t.lower() for t in structure]
    # Loop through the data categories
    for category, category_data in data.items():
        # Loop through the patterns in each category
        for item in category_data:
            patterns = item["patterns"]
            # Split the patterns string into a list of patterns
            patterns_list = patterns.split(", ")
            # Loop through the patterns in the list
            for pattern in patterns_list:
                # Check if any of the patterns are contained in the lowercase tokens
                if pattern in lower_structure:
                    # Return the corresponding response if a pattern is found
                    return item["responses"]
    # Return an empty string if no patterns are found
    return ""



# def process_message_question(messages_input):
#     print("process_message_question")
#     structure = get_structure(messages_input)
#     print("structure: ", structure)
    
#     return "Đang tìm câu trả lời"




def process_message_question(messages_input, data):
    # Get the answer to the question
    answer = get_answer(messages_input, data)
    if answer:
        # Return the answer if it is found
        return answer
    else:
        # Return a default message if no answer is found
        return "Sorry, I couldn't find an answer to that question."


def test():
    messages_input = "Tôi muốn hỏi khi nào mở cửa ngân hàng?"
    
    print("messages_input: ", messages_input)
    classify = sentence_classification.analysis_message(messages_input)
    print("classify: ", classify[0])
    data = sentence_classification.load_data('question.json')
    result = process_message_question(messages_input, data)
    print("result: ", result)
    
    
test()