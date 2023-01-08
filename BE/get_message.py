

import sentence_classification
import process_question
import check_story
from underthesea import text_normalize

def get_message_process(messages_input):
    classify = sentence_classification.analysis_message(messages_input)
    result = check_story.get_text(messages_input)
    if result == "NULL":
        result = process_question.question(messages_input)
        return result
    else:
        return result

def get_messge(messages_input):
    messages_input = text_normalize(messages_input)
    relay = get_message_process(messages_input)
    return relay
