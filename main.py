from __future__ import print_function

import google.auth
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload

import time
import pyautogui
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import undetected_chromedriver.v2 as uc
import time
import os

def upload_basic():
    """Insert new file.
    Returns : Id's of the file uploaded

    Load pre-authorized user credentials from the environment.
    TODO(developer) - See https://developers.google.com/identity
    for guides on implementing OAuth2 for the application.
    """
    creds, _ = google.auth.default()

    try:
        # create gmail api client
        service = build('drive', 'v3', credentials=creds)

        file_metadata = {'name': 'file.docx'}
        media = MediaFileUpload('file.docx',
                                mimetype='image/jpeg')
        # pylint: disable=maybe-no-member
        file = service.files().create(body=file_metadata, media_body=media,
                                      fields='id').execute()
        print(F'File ID: {file.get("id")}')

    except HttpError as error:
        print(F'An error occurred: {error}')
        file = None

    return file.get('id')


if __name__ == '__main__':
    chrome_options = uc.ChromeOptions()
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-popup-blocking")
    chrome_options.add_argument("--profile-directory=Default")
    chrome_options.add_argument("--ignore-certificate-errors")
    chrome_options.add_argument("--disable-plugins-discovery")
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("user_agent=DN")
    driver = uc.Chrome(options=chrome_options)

    driver.delete_all_cookies()

    driver.get("https://drive.google.com/drive/u/0/my-drive")
    
    email = driver.find_element("id", 'identifierId')
    email.send_keys('arykanarslan@gmail.com')
            
    nextBtn = driver.find_element("id", 'identifierNext')
    nextBtn.click()
        
    time.sleep(2)
    passwd = driver.find_element("name", 'password')
    passwd.send_keys('P@ssword!1234')
    nextBtn = driver.find_element("id", 'passwordNext')
    nextBtn.click()
            
    print("Login completed!")

    time.sleep(2)

    driver.find_element(By.XPATH, "/html/body/div[3]/div/div[3]/div/button[1]").click()  
    wait = WebDriverWait(driver, 10)
    addNewFile = wait.until(EC.element_to_be_clickable((By.XPATH, '//div[3]/div/span[2]/span/div')))
    addNewFile.click()
    time.sleep(4)

    filename = 'file.docx'

    #для мак ос
    time.sleep(2)
    pyautogui.write(os.getcwd() + '/' + filename)
    print(os.getcwd() + '/' + filename)
    pyautogui.press('enter')

    
 
    time.sleep(10)
    driver.find_element(By.XPATH, "/html/body/div[16]/div[1]/div/div/div/div/div[3]/div[2]/button/span").click()

    for i in range(20):
        try:
            addNewFile = driver.find_element(By.XPATH, "/html/body/div[3]/div/div[5]/div[2]/div[1]/div/c-wiz/div[2]/c-wiz/div[1]/c-wiz/div/c-wiz/div[1]/c-wiz/c-wiz/div/c-wiz/div/div/div")
            addNewFile.click()
            pyautogui.press('enter')
            break
        except:
            time.sleep(1)

    
    time.sleep(5)
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(5)
    body = driver.find_element(By.TAG_NAME, "body")
    body.send_keys(Keys.CONTROL + 'a')
    body.send_keys(Keys.CONTROL + Keys.SPACE)


    driver.find_element(By.XPATH, '/html/body/div[2]/div[4]/div[2]/div[1]/div[2]/div[17]/div/div/div/input').send_keys(Keys.CONTROL + 'a')
    driver.find_element(By.XPATH, '/html/body/div[2]/div[4]/div[2]/div[1]/div[2]/div[17]/div/div/div/input').send_keys(4)
    driver.find_element(By.XPATH, '/html/body/div[2]/div[4]/div[2]/div[1]/div[2]/div[17]/div/div/div/input').send_keys(Keys.ENTER)

    body.send_keys(Keys.CONTROL + 'h')
    time.sleep(4)
    driver.find_element(By.ID, 'docs-findandreplacedialog-input').send_keys(Keys.CONTROL + 'a')
    driver.find_element(By.ID, 'docs-findandreplacedialog-input').send_keys(Keys.SPACE)
    driver.find_element(By.ID, 'docs-findandreplacedialog-button-replace-all').click()

    driver.find_element(By.ID, 'docs-findandreplacedialog-use-regular-expressions').click()
    driver.find_element(By.ID, 'docs-findandreplacedialog-input').send_keys(Keys.CONTROL + 'a')
    driver.find_element(By.ID, 'docs-findandreplacedialog-input').send_keys("\\", 'n')
    driver.find_element(By.ID, 'docs-findandreplacedialog-button-replace-all').click()
    driver.find_element(By.ID, 'docs-findandreplacedialog-input').send_keys(Keys.ESCAPE)

    #here must be deliting photos!!

    driver.find_element(By.ID, 'docs-file-menu').click()    
    wait = WebDriverWait(driver, 10)
    element = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id=":6u"]')))
    element.click()

    driver.find_element(By.ID, 'kix-pagesetupdialog-margin-left').send_keys(Keys.CONTROL + 'a')
    driver.find_element(By.ID, 'kix-pagesetupdialog-margin-left').send_keys("0.55")

    driver.find_element(By.ID, 'kix-pagesetupdialog-margin-right').send_keys(Keys.CONTROL + 'a')
    driver.find_element(By.ID, 'kix-pagesetupdialog-margin-right').send_keys("5.70")
    driver.find_element(By.NAME, 'ok').click()

    time.sleep(20)
