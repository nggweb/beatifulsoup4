from bs4 import BeautifulSoup
import requests
import csv
from django.shortcuts import render
source = requests.get('http://coreyms.com').text

soup = BeautifulSoup(source, 'lxml')

csv_file = open('ngg_scrape.csv', 'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['headline', 'summary', 'video_link'])
news = []
for article in soup.find_all('article'):
    headline = article.h2.a.text
    print(headline)

    summary = article.find('div', class_='entry-content').p.text
    print(summary)

    try:
        vid_src = article.find('iframe', class_='youtube-player')['src']

        vid_id = vid_src.split('/')[4]
        vid_id = vid_src.split('/')[0]

        yt_link = f'https://youtube.com/watch?v={vid_id}'
    except Exception as e:
        yt_link = None

    print(yt_link)

    print()
    news.append({'summary': summary, 'headline': headline, 'yt_link': yt_link})
    csv_writer.writerow([headline, summary, yt_link])

csv_file.close()


def index(req):
    return render(req, 'news/index.html', {'news': news})
