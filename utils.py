# coding: utf-8

import requests


def set_headers(**kw):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
    }
    headers.update(kw)
    return headers


def fetch(url, headers=None, data=None):
    headers = set_headers() if headers is None else headers
    try:
        resp = requests.get(url, headers=headers, data=data)
        if resp.status_code == 200:
            return resp
    except Exception:
        return None
    return None

