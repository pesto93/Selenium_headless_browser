import re
import pandas as pd
import os
import time
from selenium import webdriver


# This Class uses selenium to download the latest crawler.idx file and move it to script folder


class latestCrawler(object):

    def __init__(self):
        self.url = 'https://google.com'

    def selenium(self):
        # Let's create some option to make Chromium go headless
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        options.add_argument('disable-gpu')

        # Launch the browser and make prefs
        browser = webdriver.Chrome(chrome_options=options)
        browser.command_executor._commands["send_command"] = ("POST", '/session/$sessionId/chromium/send_command')
        params = {'cmd': 'Page.setDownloadBehavior', 'params': {'behavior': 'allow', 'downloadPath': os.getcwd()}}
        browser.execute("send_command", params)
        browser.get(self.url)


we = latestCrawler()

we.selenium()
