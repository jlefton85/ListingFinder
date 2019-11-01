from bs4 import BeautifulSoup
import requests
from datetime import datetime
import os
import pickle

articles = []
dirname = os.path.dirname(__file__)
pickle_path = dirname + r"/lfpickle.pkl"

unpickler = pickle.Unpickler(dirname)
for company in unpickler.load():
    url = company.url
    html = requests.get(url)
    soup = BeautifulSoup(html.text, "html.parser")
    tags = soup.find_all()
    print(soup)

with open(dirname, 'r') as historyFile:
    history = historyFile.read()

articlesTemp = list(articles)

for article in articles:
    if article[1].strip().replace('\n',' ').replace('\r','') in history:
        articlesTemp.remove(article)

articles = list(articlesTemp)

report = str(datetime.now().replace(microsecond = 0)) + '\n'
if len(articles) == 0:
    report += "No articles found.\n"
else:
    for index, article in enumerate(articles):
        report += str(index + 1) + '. ' + article[0][0] + '\n' + article[1].strip().replace('\n',' ').replace('\r','') + '\n'
report += "\n"

pickler = pickle.Pickler(pickle_path)
