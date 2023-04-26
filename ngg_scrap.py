from bs4 import BeautifulSoup
import requests
import csv

source = requests.get('http://coreyms.com').text

soup = BeautifulSoup(source, 'lxml')

csv_file = open('ngg_scrape.csv', 'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['headline', 'summary', 'video_link'])

for article in soup.find_all('article'):
    headline = article.h2.a.text
    print(headline)

    summary = article.find('div', class_='entry-content').p.text
    print(summary)

    yt_link = None  # set yt_link to None by default

    # check if iframe with youtube-player class exists
    iframe = article.find('iframe', class_='youtube-player')
    if iframe is not None:
        try:
            vid_src = iframe['src']
            vid_id = vid_src.split('/')[4]
            vid_id = vid_id.split('?')[0]
            yt_link = f'https://youtube.com/watch?v={vid_id}'
            print(yt_link)
        except Exception as E:
            print(E)

    print(yt_link)
    print()

    csv_writer.writerow([headline, summary, yt_link])

csv_file.close()toi_r = requests.get("https://timesofindia.indiatimes.com/briefs")
toi_soup = BeautifulSoup(toi_r.content, 'html5lib')

toi_headings = toi_soup.find_all('h2')

toi_headings = toi_headings[0:-13]  # removing footers

toi_news = []

for th in toi_headings:
    toi_news.append(th.text)
