import json


def load_data(file_path):
    with open(file_path, encoding="utf8") as json_data:
        intents = json.load(json_data)

    return intents

classes = load_data('classify_document.json')
    


def analysis_message(messages_input):
    classify = []
    for i in range(len(classes['intents'])):
        for j in range(len(classes['intents'][i]['key'])):
            check = messages_input.find(classes['intents'][i]['key'][j])
            if check > 0:
                text = classes['intents'][i]['type']
                classify.append(text)

    return classify