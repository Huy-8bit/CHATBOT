#
#
# import sentence_classification
# import process_question
# import check_story
# # from underthesea import text_normalize
#
# def get_message_process(messages_input):
#     classify = sentence_classification.analysis_message(messages_input)
#     result = check_story.get_text(messages_input)
#     if result == "NULL":
#         result = process_question.question(messages_input)
#         return result
#     else:
#         return result
#
#
# def main():
#
#     while True:
#         # print(intents)
#         print("Bạn: ", end="")
#         messages_input = " " + input()
#         #messages_input = text_normalize(messages_input)
#         if 'quit' in messages_input:
#             break
#         else:
#             replay = get_message_process(messages_input)
#             print("Bot: ", replay)
#
#
# main()
