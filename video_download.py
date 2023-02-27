from bs4 import BeautifulSoup 
import requests
from urllib.request import urlopen
import ssl


def download(link,save_name):
    import requests

    cookies = {
        '_ga': 'GA1.2.1581180541.1677273838',
        '__gads': 'ID=c0c12ebb8c07e0d8-2212e44921dc00a5:T=1677273838:RT=1677273838:S=ALNI_MZuPil9BznI8z9UxQqbIFfb834fzA',
        '__cflb': '02DiuEcwseaiqqyPC5reXswsgyrfhBQemh3reA257xoij',
        '_gid': 'GA1.2.735065766.1677501335',
        '_gat_UA-3524196-6': '1',
        '__gpi': 'UID=00000bdee1c712fa:T=1677273838:RT=1677501335:S=ALNI_MYxrM9mKkwu18A_wlcscx0rylSj-g',
    }

    headers = {
        'authority': 'ssstik.io',
        'accept': '*/*',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'cookie': '_ga=GA1.2.1581180541.1677273838; __gads=ID=c0c12ebb8c07e0d8-2212e44921dc00a5:T=1677273838:RT=1677273838:S=ALNI_MZuPil9BznI8z9UxQqbIFfb834fzA; __cflb=02DiuEcwseaiqqyPC5reXswsgyrfhBQemh3reA257xoij; _gid=GA1.2.735065766.1677501335; _gat_UA-3524196-6=1; __gpi=UID=00000bdee1c712fa:T=1677273838:RT=1677501335:S=ALNI_MYxrM9mKkwu18A_wlcscx0rylSj-g',
        'hx-current-url': 'https://ssstik.io/en',
        'hx-request': 'true',
        'hx-target': 'target',
        'hx-trigger': '_gcaptcha_pt',
        'origin': 'https://ssstik.io',
        'referer': 'https://ssstik.io/en',
        'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
    }

    params = {
        'url': 'dl',
    }

    data = {
        'id': link,
        'locale': 'en',
        'tt': 'dDJueGQ3',
    }

    response = requests.post('https://ssstik.io/abc', params=params, cookies=cookies, headers=headers, data=data)
    print('loading response')
    download_soup=BeautifulSoup(response.text,"html.parser")
    print('parsing response')
    download_link=download_soup.a["href"]
    print('creating download link')
    context = ssl._create_unverified_context()
    mp4_file=urlopen(download_link,context=context)
    print('getting mp4')
  
    with open(f'videos/{save_name}.mp4','wb' ) as output:
        while True:
            data=mp4_file.read(4096)
            if data:
                output.write(data)
            else:
                print('done')
                break
link=input("Enter Tiktok Link:\n")
name=input("Write the name you want to save it as\n")
download(link,name)  
    