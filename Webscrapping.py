from bs4 import BeautifulSoup
import requests
import csv

#source = requests.get('https://coreyms.com/').text

#soup = BeautifulSoup(source, 'lxml')

#print(soup.prettify())


# grab one video information

# printing the first artilce

#article  = soup.find('article')
#print(article.prettify())

#headline = article.h2.a.text
#print(headline)

#summary = article.find('div', class_= 'entry-content').p.text
#print(summary)

#video_source = article.find('iframe', class_ ='youtube-player')['src']
#print(video_source)

#video_id = video_source.split('/')[4]
#video_id = video_id.split('?')[0]
#print(video_id)

#Creating my own youtube link using the video id

#youtube_link = f'https://youtube.com/watch?v={video_id}'
#print(youtube_link)

# To print all the articles and youtube links on the webpage

source = requests.get('https://coreyms.com/').text
soup = BeautifulSoup(source, 'lxml')
csv_file = open('joescrapped.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['headline', 'summary', 'Video Link'])

for article in soup.find_all('article'):
    headline = article.h2.a.text
    print(headline)
    summary = article.find('div', class_='entry-content').p.text
    print(summary)

    try:
        video_source = article.find('iframe', class_ ='youtube-player')['src']
        video_id = video_source.split('/')[4]
        video_id = video_id.split('?')[0]
        youtube_link = f'https://youtube.com/watch?v={video_id}'
    except Exception as e:
        youtube_link = None
    print(youtube_link)
          
    print()
    csv_writer.writerow([headline, summary, youtube_link])

csv_file.close()

# Save the page to a CSV File

# if the webiste is edited.

    
    
