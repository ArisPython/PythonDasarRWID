import requests

url = 'https://detik.com'
try:
    response = requests.get(url)
    if response.status_code == 200:
        print(f'sukses dengan kode response {response.status_code}')
        print(f'hasil scrap homepage {response.text}')
    else:
        print(f'ada kesalahan/error dengan kode response {response.status_code}')
except Exception as e:
    print(f'ada yang salah, {e}')
print('program ended')
