import requests
from bs4 import BeautifulSoup
import json

start_url = 'https://stackoverflow.com/questions/?tab=newest&pagesize='

for page_num in range(1, 10):
    url = start_url + str(page_num)

    response = requests.get(url)
    content = BeautifulSoup(response.text, 'lxml')
    
    links = content.findAll('a', {'class': 'question-hyperlink'})
    description = content.findAll('div', {'class': 'excerpt'})

    print(len(links), len(description))
    print('\n\nURL:', url)

    for index in range(0, len(description)):
        question = {
            'title': links[index].text,
            'url': links[index]['href'],
            'description': description[index].text.strip().replace('\n', ' ')
        }

        print(json.dumps(question, indent=2))