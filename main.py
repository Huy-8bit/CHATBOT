

import sentence_classification
import process_question




def get_message_process(messages_input):
    classify = sentence_classification.analysis_message(messages_input)
    print("classify: ", classify)
    if 'question' in classify:
        return process_question.process_message_question(messages_input)
    elif 'greet' in classify:
        return "Chào bạn, tôi có thể giúp gì cho bạn"
    elif 'request' in classify:
        return "Bạn muốn tôi giúp gì cho bạn?"

    elif 'exclamatory' in classify:
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
            