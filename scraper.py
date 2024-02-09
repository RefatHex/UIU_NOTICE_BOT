import requests
from bs4 import BeautifulSoup

url = 'https://www.uiu.ac.bd/'  

previous_title = "" 


def get_notices():
    global previous_title 

    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        notices = soup.find_all('a', class_='single-notice')

        date = notices[0].find('h6', class_='subtitle').get_text()
        title = notices[0].find('h4', class_='title').get_text()
        link = notices[0]['href']

        if previous_title != title:  
            previous_title = title
            return f'Date:  {date}\nTitle: {title}\nLink: {link}'
        else:
            return None  

