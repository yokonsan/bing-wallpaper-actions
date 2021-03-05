# coding: utf-8

import os
import time


read_me_body = """# Bing wallpaper actions

Today's wallpaper.

![{filename}.jpg](papers/{filename}.jpg)

Enjoy it.
"""


def update():
    date_str = time.strftime("%Y%m%d", time.localtime())
    read_me_file = os.path.join(os.path.abspath('.'), 'README.md')
    with open(read_me_file, 'w') as w:
        w.write(read_me_body.format(filename=date_str))


if __name__ == "__main__":
    update()
