import sentence_classification

json1 = sentence_classification.load_data('story.json')
json2 = sentence_classification.load_data('story1.json')

data = sentence_classification.load_data('story.json')


def lower_strings(data):
    for value in data['data']:
        for i in range(len(value['story'])):
            for j in range(len(value['story'][i]['patterns'])):
                value['story'][i]['patterns'][j] = value['story'][i]['patterns'][j].lower()
            for j in range(len(value['story'][i]['responses'])):
                value['story'][i]['responses'][j] = value['story'][i]['responses'][j].lower()


lower_strings(data)


def get_response(input_text, data):
    for value in data['data']:
        for i in range(len(value['story'])):
            for j in range(len(value['story'][i]['patterns'])):
                if input_text == value['story'][i]['patterns'][j]:
                    if value['story'][i]['responses']:
                        return value['story'][i]['responses'][0]

    return "NULL"


def add_response(input_text, result, tag, data):

    # check result
    for value in data['data']:
        for i in range(len(value['story'])):
            for j in range(len(value['story'][i]['responses'])):
                if result == value['story'][i]['responses'][j]:
                    print("This response is exist")
                    value['story'][i]['patterns'].append(input_text)
                    sentence_classification.write_data('story.json', data)
                    return
    # check tag
    for value in data['data']:
        if tag == value['tag']:
            value['story'].append(
                {"patterns": [input_text], "responses": [result]})
            sentence_classification.write_data('story.json', data)
            return
    # add new tag
    data['data'].append(
        {"tag": tag, "story": [{"patterns": [input_text], "responses": [result]}]})
    sentence_classification.write_data('story.json', data)


def get_text(input_text):

    if input_text == "exit":
        return "exit"

    result = get_response(input_text, data)

    if result == "NULL":
        print("Don't have this story")

    else:
        print("Bot: ", result)

    return result


for value in json2['data']:
    tag = value['tag']
    patterns = ""
    responses = ""
    for i in range(len(value['story'])):
        for j in range(len(value['story'][i]['patterns'])):
            patterns = value['story'][i]['patterns'][j]
            responses = value['story'][i]['responses'][0]
            print("User: ", patterns)
            result = get_text(patterns)
            if result == "NULL":
                add_response(patterns, responses, tag, data)
                print("Add new story")
            else:
                print(result)

print("Done")
