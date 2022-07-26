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
import io

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

    #chrome_options.headless = True
    #chrome_options.add_argument('--headless')

    driver = uc.Chrome(options=chrome_options)
    driver.delete_all_cookies()

    driver.get("https://drive.google.com/drive/folders/1GWArUb9GIuI8OdS6dd9CFl8PODe3zjv8")

    email = driver.find_element("id", 'identifierId')
    email.send_keys('arykanarslan@gmail.com')
            
    nextBtn = driver.find_element("id", 'identifierNext')
    nextBtn.click()
        
    time.sleep(2)
    #driver.save_screenshot("screenshot.png")
    
    passwd = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input')
    passwd.send_keys('P@ssword!1234')
    nextBtn = driver.find_element("id", 'passwordNext')
    nextBtn.click()
            
    print("Login completed!")
    time.sleep(3)

    driver.get("https://docs.google.com/document/d/" + r['id'] + "/edit")

    #wait = WebDriverWait(driver, 10)
    #folder = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div/div[5]/div[2]/div[2]/div/c-wiz/div[2]/c-wiz/div[1]/c-wiz/div/c-wiz/div[1]/c-wiz/c-wiz/div/c-wiz/div/div")))
    #folder.click()
    
    time.sleep(9)
    body = driver.find_element(By.TAG_NAME, "body")
    body.send_keys(Keys.COMMAND + 'a') #control // COMMAND
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

    #here must be deliting photos!!

    time.sleep(2)

    driver.find_element(By.ID, 'docs-file-menu').click()    

    element = driver.find_element(By.ID, ':6u')
    driver.implicitly_wait(10)
    ActionChains(driver).move_to_element(element).click(element).perform()

    driver.find_element(By.ID, 'kix-pagesetupdialog-margin-left').send_keys(Keys.COMMAND + 'a')
    driver.find_element(By.ID, 'kix-pagesetupdialog-margin-left').send_keys("0.55")

    driver.find_element(By.ID, 'kix-pagesetupdialog-margin-right').send_keys(Keys.COMMAND + 'a')
    driver.find_element(By.ID, 'kix-pagesetupdialog-margin-right').send_keys("5.70")
    driver.find_element(By.NAME, 'ok').click()

    time.sleep(10)

    file_id = r['id']
    request = service.files().get_media(fileId=file_id)
    filename = os.getcwd() + '/result/print_shpora.docx'
    fh = io.FileIO(filename, 'wb')
    downloader = MediaIoBaseDownload(fh, request)
    done = False
    while done is False:
            status, done = downloader.next_chunk()
            print ("Download %d%%." % int(status.progress() * 100))
    time.sleep(1)

    service.files().delete(fileId=file_id).execute()
    print("File deleted!")
