import requests
from time import sleep


def download_site(url, session, i):
    with session.get(url) as response:
        r = response.content
        with open(f'./artifacts/{i}.jpeg', 'wb') as f:
            f.write(r)


def download_all_sites():
    with requests.Session() as session:
        for i in range(5):
            sleep(0.5)
            download_site('https://thisartworkdoesnotexist.com/', session, i)


if __name__ == "__main__":
    download_all_sites()
