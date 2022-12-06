import requests
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=M&rtm=N&ymd=20210701',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')
# 코딩 시작

mysics = soup.select('#body-content > div.newest-list > div > table > tbody > tr')
for music in mysics:
    title = music.select_one('td.info > a.title.ellipsis').text.strip()

    rank = music.select_one('td.number').text[0:2].strip()
    if rank in ['1','2','3','4','5','6','7','8','9']:
        rank = rank.rjust(0)
    singer = music.select_one('td.info > a.artist.ellipsis').text
    if title.startswith('19금'):
        title = title.replace('19금', '').lstrip()
    print(rank, title, singer)



