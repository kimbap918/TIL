# 9917f46b6425e1df8108a68c4d9202b0
# https://api.themoviedb.org/3/movie/76341?api_key=<<api_key>>
# 반복해서 줘야하는구나 
from pprint import pprint
import requests
# BASE_URL = 'https://api.themoviedb.org/3'
# path = '/movie/now_playing'
# params = {
#     'api_key': '9917f46b6425e1df8108a68c4d9202b0',
#     'language': 'ko-KR'
# }

# response = requests.get(BASE_URL+path, params=params).json()
# pprint(response)

for n in range(1, 1024):
    URL = f'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo={n}'
    response = requests.get(URL).json()
    pprint(response)