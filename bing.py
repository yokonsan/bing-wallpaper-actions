# coding: utf-8

import logging

from utils import fetch
from settings import config


def get_img_url():
    response = fetch(config.BING_IMG_URL)
    if response:
        data = response.json
        try:
            img_url = data['images'][0]['url']
            return img_url
        except KeyError:
            logging.warn('parse error...')
            return None
    return None


def saver(content):
    date_str = ''
    with open(f'{date_str}.jpg') as target:
        pass


def download():
    url = get_img_url()
    if not url:
        logging.warn('get image url error...')
        return None
    
    response = fetch(url)
    if response:
        content = response.content


if __name__ == "__main__":
    pass
