import csv
import numpy as np
import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup
page_link = 'https://www.mxplayer.in/movies'
html = urlopen(page_link)
soup = BeautifulSoup(html, 'lxml')
page_response = requests.get(page_link, timeout=5)
page_content = BeautifulSoup(page_response.content, "html.parser")

links=[]
all_links = soup.findAll('div',attrs={"class":"card-wrapper"})
for link in all_links:
    x=link.findChild("a")
    links.append(x.get("href"))


years_lang=[]
langs_years =soup.findAll('div',attrs={"class":"text-overflow card-subheader"})
for url_year in langs_years:
    years_lang.append(url_year.text)

titles=[]
movie_title=soup.findAll('div',attrs={"class":"text-overflow card-header"})
for title in movie_title:
    titles.append(title.text)

links = np.array(links)

with open('outputFile.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    writer.writerow(['URL', 'title','type_language_year'])
    for row in range(0,links.shape[0]):
        myList = []
        myList.append(links[row])
        myList1=[]
        myList1.append(titles[row])
        myList2 = []
        myList2.append(years_lang[row])
        writer.writerow([myList[0],myList1[0],myList2[0]])

