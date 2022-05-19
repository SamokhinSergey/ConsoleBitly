import os
import requests
from dotenv import load_dotenv
from urllib.parse import urlparse
import argparse
load_dotenv()


def get_link():
    parser = argparse.ArgumentParser(
        description='Bitly console utility'
    )
    parser.add_argument('link',
                        help="Link to web with http/s) ",
                       )
    args = parser.parse_args()
    return args.link


def count_clicks(token, user_url):
    bitly_api = f"https://api-ssl.bitly.com/v4/bitlinks/{user_url}/clicks/summary"
    headers = {
        'Authorization': f"Bearer {token}",
    }
    payload = {
        "units": "-1",
    }
    bitly_response = requests.get(bitly_api, headers=headers, params=payload)
    bitly_response.raise_for_status()
    return bitly_response.json()['total_clicks']


def get_shorten_link(token, user_url):
    bitly_api = "https://api-ssl.bitly.com/v4/bitlinks"
    headers = {
       'Authorization': f"Bearer {token}",
    }

    payload = {
        "long_url": user_url
    }
    bitly_response = requests.post(bitly_api, headers=headers, json=payload)
    bitly_response.raise_for_status()
    return bitly_response.json()['link']


def is_bitlink(token, user_url):
    bitly_api = f"https://api-ssl.bitly.com/v4/bitlinks/{user_url}"
    headers = {
      'Authorization': f"Bearer {token}",
    }
    bitly_response = requests.get(bitly_api, headers=headers)
    return bitly_response.ok
        

if __name__ == '__main__':
    bitly_token = os.environ['BITLY_TOKEN']
    user_url = get_link()
    parsed_url = urlparse(user_url)
    try:
        trimmed_url = f"{parsed_url.netloc}{parsed_url.path}"
    except TypeError:
        raise SystemExit("Не верно введена ссылка")
    try:
        if is_bitlink(bitly_token, trimmed_url):
            counter = count_clicks(bitly_token, trimmed_url)
            print("Вы ввели уже существующую ссылку с bitly.")
            print(f"По этой ссылке перешли {counter} раз.")
        else:
            bitlink = get_shorten_link(bitly_token, user_url)
            print("Вы ввели ссылку на сайт для сокращения ее на bitly")
            print('Вот ее битлинк:', bitlink)
    except requests.exceptions.HTTPError:
            print(trimmed_url)
            raise SystemExit("Возникли проблемы с подключением к bitly")
