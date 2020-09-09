import requests
from bs4 import BeautifulSoup

url = 'https://detik.com'
try:
    response = requests.get(url)
    if response.status_code == 200:
        print(f'sukses dengan kode response {response.status_code}')
        #print(f'hasil scrap homepage {response.text}')
        soup = BeautifulSoup(response.text, features="html.parser")
        print(f'hasil pemanggilan: {url}')
        print(f'Title : {soup.title.string}')
    else:
        print(f'ada kesalahan/error dengan kode response {response.status_code}')
except Exception as e:
    print(f'ada yang salah, {e}')
print('program ended')
