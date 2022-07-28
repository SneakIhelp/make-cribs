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
from google.oauth2 import service_account
from googleapiclient.http import MediaIoBaseDownload,MediaFileUpload
from googleapiclient.discovery import build
from google_drive_downloader import GoogleDriveDownloader as gdd
import io
import urllib.request

if __name__ == '__main__':
    print("Перед тем как начать: \n" +
        "1) Запустите в ворде ваш файл \n" + 
        "2) Откройте режим найти и заменить (ctrl + h) \n" +
        "3) Введите '^p' без кавычек \n" +
        "4) Замените всё найденное \n" +
        "5) Загрузите файл с любым английским названием заканчивающемся на '.docx' в папку с файлом main.py")
    
    print(input("Нажмите enter, если вы готовы: "))
    print()


    SCOPES = ['https://www.googleapis.com/auth/drive']

    fold = os.getcwd()
    files = os.listdir(fold)
    json = [i for i in files if i.endswith('.json')]

    SERVICE_ACCOUNT_FILE = str(os.path.abspath(json[0]))
    credentials = service_account.Credentials.from_service_account_file(
            SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    service = build('drive', 'v3', credentials=credentials)

    folder_id = '1GWArUb9GIuI8OdS6dd9CFl8PODe3zjv8'
    docx = [i for i in files if i.endswith('.docx')]

    name = docx[0]
    file_path = os.path.abspath(name)
    nondocx_name = os.path.splitext(name)[0]
    file_metadata = {
                    'name': name,
                    'parents': [folder_id]
                }
    media = MediaFileUpload(file_path, resumable=True)
    r = service.files().create(body=file_metadata, media_body=media, fields='id').execute()
    print(r)
    print('File uploaded successfully!')

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

    driver.get("https://docs.google.com/document/d/" + r['id'] + "/edit")


    time.sleep(9)
    body = driver.find_element(By.TAG_NAME, "body")
    body.send_keys(Keys.COMMAND + 'a') #CONTROL // COMMAND
    body.send_keys(Keys.COMMAND + Keys.SPACE)

    time.sleep(3)
    driver.find_element(By.XPATH, '/html/body/div[2]/div[4]/div[2]/div[1]/div[2]/div[17]/div/div/div/input').send_keys(Keys.COMMAND + 'a')
    time.sleep(1)
    driver.find_element(By.XPATH, '/html/body/div[2]/div[4]/div[2]/div[1]/div[2]/div[17]/div/div/div/input').send_keys(4)
    driver.find_element(By.XPATH, '/html/body/div[2]/div[4]/div[2]/div[1]/div[2]/div[17]/div/div/div/input').send_keys(Keys.ENTER)

    #body.send_keys(Keys.CONTROL + 'h') #WIN
    body.send_keys(Keys.COMMAND + Keys.SHIFT + 'h')
    time.sleep(4)
    driver.find_element(By.ID, 'docs-findandreplacedialog-input').send_keys(Keys.COMMAND + 'a')
    driver.find_element(By.ID, 'docs-findandreplacedialog-input').send_keys(Keys.SPACE)
    driver.find_element(By.ID, 'docs-findandreplacedialog-button-replace-all').click()

    driver.find_element(By.ID, 'docs-findandreplacedialog-use-regular-expressions').click()
    driver.find_element(By.ID, 'docs-findandreplacedialog-input').send_keys(Keys.COMMAND + 'a')
    driver.find_element(By.ID, 'docs-findandreplacedialog-input').send_keys("\\", 'n')
    driver.find_element(By.ID, 'docs-findandreplacedialog-button-replace-all').click()
    driver.find_element(By.ID, 'docs-findandreplacedialog-input').send_keys(Keys.ESCAPE)


    time.sleep(2)

    driver.find_element(By.ID, 'docs-file-menu').click()    

    element = driver.find_element(By.ID, ':6u')
    driver.implicitly_wait(10)
    ActionChains(driver).move_to_element(element).click(element).perform()

    driver.find_element(By.ID, 'kix-pagesetupdialog-margin-left').send_keys(Keys.COMMAND + 'a')
    driver.find_element(By.ID, 'kix-pagesetupdialog-margin-left').send_keys("0.65")

    time.sleep(2)

    driver.find_element(By.ID, 'kix-pagesetupdialog-margin-right').send_keys(Keys.COMMAND + 'a')
    driver.find_element(By.ID, 'kix-pagesetupdialog-margin-right').send_keys("15")
    driver.find_element(By.NAME, 'ok').click()

    time.sleep(5)
    print("Форматирование произведено успешно!")

    driver.close()

    time.sleep(10)
                                    
    fileid = r['id']
    url = f'https://docs.google.com/document/d/{fileid}/export?format=docx&id={fileid}'
    urllib.request.urlretrieve(url, './result/file.docx')

    print("File deleted!")
