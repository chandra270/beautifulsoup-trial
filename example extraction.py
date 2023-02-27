from bs4 import BeautifulSoup
import requests
import csv
import time
url = "https://www.postjobfree.com/resumes?l=Kochi%2C+Kerala%2C+India&r=10&t=python+developer&radius=50"
response = requests.get(url)
soup = BeautifulSoup(response.content,'html.parser')
title_tags = soup.find_all('h3',attrs={'class':'itemTitle'})
links=["https://www.postjobfree.com"+ title_tag.a['href'] for title_tag in title_tags]
results=[]
for link in links:
    res = requests.get(link)
    print(res.status_code, link)
    content = BeautifulSoup(res.content, 'html.parser')
    results.append({
        'job_title':content.find('div', attrs={'class':'leftColumn'}).find('h1').get_text(),
        'resume':content.find('div', attrs={'class':'normalText'}).get_text(),
    })
    time.sleep(3)
with open('resumeex.csv','w',encoding='utf-8',newline='') as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=results[0].keys())
    writer.writeheader()
    for row in results:
        writer.writerow(row)