import json


def load_data(file_path):
    with open(file_path, encoding="utf8") as json_data:
        intents = json.load(json_data)

    return intents

def write_data(file_path, data):
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
        


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