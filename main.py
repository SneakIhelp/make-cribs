from pywinauto.application import Application
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd
import psutil
import os
import time
from bs4 import BeautifulSoup
from unittest import TestCase
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options


option = Options()
option.add_argument("--disable-infobars") 
browser = webdriver.Chrome('C:\webdr\chromedriver.exe', chrome_options=option)
browser.get('https://rollmyfile.com')

inpFile =  browser.find_element(by = By.CLASS_NAME, value = 'choose-btn dz-clickable')
inpFile.click()


class ForUpload(TestCase):
    def upload_file(self, filename):
            path = os.path.join(
                os.path.realpath('.'),
                'fixtures',
                filename
            )
            assert os.path.exists(path)

            for i in range(10):
                app = Application()
                app.connect(process=self.get_pid())  # connect to browser
                dialog = app.top_window_()           # get active top window (Open dialog)
                if not dialog.Edit.Exists():         # check if Edit field is exists
                    time.sleep(1)                    # if no do again in 1 second (waiting for dialog after click)
                    continue
                dialog.Edit.TypeKeys('"{}"'.format(path))   # put file path
                dialog['&OpenButton'].Click()               # click Open button

                return

            raise Exception('"Open File" dialog not found')


    def upload(self):
        el_logo_upload = self.wait.until(
        EC.presence_of_element_located(
                (By.NAME, 'upload-logo')
            )
        )

        el_logo_upload.click()
        self.upload_file('file.docx')

