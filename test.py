import sentence_classification

import json

def lower_strings(data):
    for value in data['data']:
        for result in value['story']:
            for i in range(len(result['patterns'])):
                result['patterns'][i] = result['patterns'][i].lower()
            for i in range(len(result['responses'])):
                result['responses'][i] = result['responses'][i].lower()
    return data                
                
data = sentence_classification.load_data('story.json')

new_data = lower_strings(data)


def write(data):
    with open("data.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

print (new_data)
write(new_data)