#print file chatbot.py

def file_reader(file):
    with open(file,'r') as infile:
        table = [row for row in infile]
    return table

result = file_reader('chatbot.py')

print(result)