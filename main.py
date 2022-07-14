if __name__ == '__main__':
    import time
    import pyautogui
    from selenium.webdriver.common.by import By
    from selenium.webdriver.common.action_chains import ActionChains
    from selenium.common.exceptions import NoSuchElementException
    from selenium.webdriver.support.ui import WebDriverWait 
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.support import expected_conditions as EC
    import undetected_chromedriver.v2 as uc
    import random,time,os,sys

    #options = webdriver.ChromeOptions()
    #driver = webdriver.Chrome(options=options, executable_path=r"C:\webdr\chromedriver.exe")

    chrome_options = uc.ChromeOptions()
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-popup-blocking")
    chrome_options.add_argument("--profile-directory=Default")
    chrome_options.add_argument("--ignore-certificate-errors")
    chrome_options.add_argument("--disable-plugins-discovery")
    #chrome_options.add_argument("--incognito")
    chrome_options.add_argument("user_agent=DN")
    driver = uc.Chrome(options=chrome_options)

    #driver.delete_all_cookies()

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
    addNewFile = driver.find_element(By.XPATH, "//div[3]/div/span[2]/span/div")
    addNewFile.click()
    time.sleep(2)

    filename = 'file.docx'

    pyautogui.write("C:\\Users\\Admin\\git\\py\\make-cribs\\" + filename)
    pyautogui.press('enter')
    time.sleep(2)
    pyautogui.press('enter')
    driver.find_element(By.XPATH, "/html/body/div[16]/div[1]/div/div/div/div/div[3]/div[2]/button/span").click()

    for i in range(20):
        try:
            addNewFile = driver.find_element(By.XPATH, "/html/body/div[3]/div/div[5]/div[2]/div[1]/div/c-wiz/div[2]/c-wiz/div[1]/c-wiz/div/c-wiz/div[1]/c-wiz/c-wiz/div/c-wiz/div/div/div")
            addNewFile.click()
            pyautogui.press('enter')
            break
        except:
            time.sleep(1)

    """while True:
        try:
            driver.find_element(By.XPATH, '/html/body/div[2]/div[4]/div[2]/div[1]/div[2]/div[17]/div/div/div/input')
            break
        except NoSuchElementException:
            print("NO!")
            continue"""
    
    time.sleep(5)
    ActionChains(driver).send_keys(Keys.CONTROL, Keys.TAB)
    time.sleep(5)
    ActionChains(driver).send_keys(Keys.CONTROL, 'a')

    driver.find_element(By.XPATH, '/html/body/div[2]/div[4]/div[2]/div[1]/div[2]/div[17]/div/div/div/input').sendKeys(4)

    time.sleep(20)