# coding: utf-8

import os
import logging
import time

from utils import fetch
from settings import config


def get_img_url():
    response = fetch(config.BING_IMG_URL)
    if response:
        data = response.json()
        try:
            img_url = data['images'][0]['url']
            return config.BING_HOST + img_url
        except KeyError:
            logging.warn('parse error...')
            return None
    return None


def saver(content):
    date_str = time.strftime("%Y%m%d", time.localtime())
    paper_name = os.path.join(os.path.abspath('.'), 'papers', f'{date_str}.jpg')
    with open(paper_name, 'wb') as w:
        w.write(content)


def download():
    url = get_img_url()
    if not url:
        logging.warn('get image url error...')
        return None
    
    response = fetch(url)
    if response:
        content = response.content
        saver(content)
        return True
    logging.warn('get image url error...')
    return False


if __name__ == "__main__":
    download()
