import requests
from bs4 import BeautifulSoup

link = "https://www.mechta.kz/section/smartfony/"

response = requests.get(link).text
soup = BeautifulSoup(response, 'lxml')

items = soup.find('div', class_='tw-grid tw-grid-cols-3 tw-gap-6 tw-mt-5')
title = items.find_all('div', class_='tw-mt-[15px] tw-font-normal tw-text-sm tw-text-color1 dark:tw-text-dColor1 tw-overflow-hidden tw-text-ellipsis tw-whitespace-nowrap')
price = items.find_all('div', class_='tw-text-xl tw-font-bold tw-text-color1 dark:tw-text-dColor1')

for i in range(len(title)):
    with open('text.txt', 'w', encoding='utf-8') as file:
        file.write(f'{title[i].text} - {price[i].text}\n')