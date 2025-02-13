import requests
from bs4 import BeautifulSoup
from flask import (
    request,
    redirect,
    render_template,
    Flask
)

app = Flask(__name__)

link = "https://www.olx.kz/transport/legkovye-avtomobili/kar/"

response = requests.get(link).text


soup = BeautifulSoup(response, 'lxml')

main_div = soup.find('div', class_='css-j0t2x2')

title_div = main_div.find_all('h4', class_='css-1sq4ur2')

price_div = main_div.find_all('p', class_='css-6j1qjp')

import re

def calc(price_div):
    prices = []
    for price in price_div:
        price_text = price.text
        price_value = re.sub(r'[^\d]', '', price_text)
        if price_value:
            prices.append(int(price_value))
    
    if prices:
        return sum(prices) / len(prices)
    return 0




@app.route("/", methods=["GET", "POST"])
def get_home():
    if request.method == 'POST':
        average_price = calc(price_div)
        return render_template('index.html', title_div=title_div, price_div=price_div, average_price=average_price)
    return render_template("index.html")










if __name__ == "__main__":
    app.run(debug=True)