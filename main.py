from bs4 import BeautifulSoup
import requests
import csv

source = requests.get('https://coreyms.com').text
soup = BeautifulSoup(source, 'lxml')

csv_file = open('cms_scrape.csv', 'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['headline', 'summary', 'video_link'])


for article in soup.find_all('article'):

    headline = article.h2.a.text
    summary = article.find('div', class_= 'entry-content').p.text

    try:
        link = article.find('iframe', class_='youtube-player')['src']
        id = link.split('/')
        id = id[4].split('?')
        vid_id = id[0]

        yt_link = f'https://www.youtube.com/watch?v={vid_id}'

    except:
        yt_link = None

    print(headline)
    print(summary)
    print(yt_link)
    print()

    csv_writer.writerow([headline, summary, yt_link])

csv_file.close()
