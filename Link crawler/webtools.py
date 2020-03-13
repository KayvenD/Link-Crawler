#!/usr/bin/env python

import re
import pyperclip
import subprocess
from datetime import datetime

class webinspector:
    def inspect_html(webcontent,domain):

        ##domain = 'www.ahzixun.cn'

        ##correct web file systems
        stripped = re.sub('<img src="/', '<img src="', webcontent)
        stripped = re.sub('content=', 'content="', stripped)
        stripped = re.sub('=""', '="', stripped)
        stripped = re.sub('//' + domain + '/', "", stripped)
        stripped = re.sub('/>', '>', stripped)
        stripped = re.sub('; >', ';">', stripped)
        stripped = re.sub('"  alt="', '" alt="', stripped)
        stripped = re.sub('" >', '">', stripped)
        stripped = re.sub('<script src="/', '<script src="', stripped)
        stripped = re.sub('"  title="', '" title="', stripped)
        stripped = re.sub('<link rel="canonical" href="http:', '<link rel="canonical" href="index.html', stripped)
        stripped = re.sub('src="/', 'src="', stripped)
        stripped = re.sub('type="text/css" rel="stylesheet" href="/', 'type="text/css" rel="stylesheet" href="', stripped)
        stripped = re.sub('href="/index.html"', 'href="index.html"', stripped)
        #print(stripped)
        pyperclip.copy(stripped)
        #copy = pyperclip.paste()
        return stripped


class M3U8:
    def download(__url:str, __file:str):
        subprocess.call('ffmpeg -i '+ __url + " " + __file, shell = True)


class download_media:

    def video(__last_item: str):
        now = datetime.now()
        time = now.strftime("%m%d%Y%H%M%S")
        __last_item = __last_item.replace("\n\r", "")
        __last_item = __last_item.replace("\n", "")
        M3U8.download(__last_item, "video" + time + ".mp4")
        print(__last_item + " Download done!")

# #**************** for debugging purpose only ********************
# domain = 'www.ahzixun.cn'
# resp = req.get("http://www.ahzixun.cn")
# print(resp.encoding)
# ncontent = str(resp.content, '<UTF-8>', errors='replace')
# print(webinspector.inspect_html(ncontent))


