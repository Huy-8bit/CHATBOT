import json
import sentence_classification


def ratio_of_matches(sentence1, sentence2):
    # Split the sentences into lists of words
    words1 = sentence1.split()
    words2 = sentence2.split()
    matches = 0
    for word in words1:
        if word in words2:
            matches += 1
    return matches / len(words1)


def lower_strings(data):
    for value in data['data']:
        for i in range(len(value['story'])):
            for j in range(len(value['story'][i]['patterns'])):
                value['story'][i]['patterns'][j] = value['story'][i]['patterns'][j].lower()
            for j in range(len(value['story'][i]['responses'])):
                value['story'][i]['responses'][j] = value['story'][i]['responses'][j].lower()


def get_response(input_text, data):
    list = [
        {"responses": "NULL",
         "ratio": 0}
    ]
    result = {"responses": "NULL", "ratio": 0}
    for value in data['data']:
        for i in range(len(value['story'])):
            for j in range(len(value['story'][i]['patterns'])):
                # if input_text == value['story'][i]['patterns'][j]:
                if ratio_of_matches(input_text, value['story'][i]['patterns'][j]) > 0.7:
                    if value['story'][i]['responses']:
                        result['responses'] = value['story'][i]['responses'][0]
                        result['ratio'] = ratio_of_matches(input_text, value['story'][i]['patterns'][j])
                        list.append(result)
                        return value['story'][i]['responses'][0]
    for i in range(len(list)):
        if list[i]['ratio'] > result['ratio']:
            result['responses'] = list[i]['responses']
            result['ratio'] = list[i]['ratio']
    return result['responses']


def get_text(input_text):
    data = sentence_classification.load_data('story.json')
    lower_strings(data)
    result = get_response(input_text, data)
    return result
