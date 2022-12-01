# from bs4 import BeautifulSoup
# import requests
# import pandas as pd
# import csv

# wiki_url = "https://vi.wiktionary.org/wiki/Th%E1%BB%83_lo%E1%BA%A1i:Th%C3%A1n_t%E1%BB%AB_ti%E1%BA%BFng_Vi%E1%BB%87t"
# file_path = "Thán từ.txt"
# f = open(file_path, 'w', encoding='utf-8')

# for i in range(1, 200):
#     print("Page: ", i, "--", wiki_url)
#     request_result = requests.get(wiki_url)
#     soup = BeautifulSoup(request_result.content, 'html.parser')
#     links = soup.find('div', {'id': 'mw-pages'})
#     new = links.find('div', {'class': 'mw-content-ltr'})
#     f.write(new.getText())
#     break
#     new1 = soup.findAll('a', {'title': 'Thể loại:Phó từ tiếng Việt'})
#     new3 = [link.get('href') for link in new1]
#     wiki_url = "https://vi.wiktionary.org" + new3[1]


# read file Đại từ.txt

def load_data(file_name):
    with open(file_name, 'r', encoding='utf-8') as f:
        data = f.read()
    return data


file_path = "Tính từ.txt"

list_results = []
for line in load_data(file_path).splitlines():
    list_results.append(line)

# print(list_results[2])


# remove duplicate
def remove_duplicate(list):
    list = sorted(set(list))
    return list

list_results = remove_duplicate(list_results)

f = open("new" + file_path, 'w', encoding='utf-8')
for word in list_results:
    f.write(word + "\n")    
f.close()
