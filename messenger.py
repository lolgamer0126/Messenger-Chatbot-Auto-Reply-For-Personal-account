from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
import pyfiglet
from printy import printy
import time 

def login(email, passwd):
    
    driver.maximize_window()
    driver.get("https://messenger.com")
    emailInput = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(("name", "email")))
    passwdInput = driver.find_element("name", "pass")
    submitButton = driver.find_element("name", 'login')
    emailInput.send_keys(email)
    passwdInput.send_keys(passwd)
    submitButton.click()
    print(driver.current_url)
    if(driver.current_url == "https://www.messenger.com/login/password/"):
        printy("OOPS! wrong credentials", "rB")
        quit()

def sendMessage(message):
    
    firstProfile = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(("xpath", '//*[@id="jsc_c_c"]/div/div/div/div/div[2]/div/div[1]/div/div[1]/a')))
    actions = ActionChains(driver)
    previous = firstProfile.text
    while(True):
        check = driver.find_element("xpath", '//*[@id="jsc_c_c"]/div/div/div/div/div[2]/div/div[1]/div/div[1]/a')
        if(check.text[0:5] != previous and "You" not in  check.text):
            check.click()
            time.sleep(1)
            actions.send_keys(message)
            actions.perform()
            actions.send_keys(Keys.ENTER)
            actions.perform()
            previous = check.text[0:5]
            print("Text arrived")
        time.sleep(1)
        

def main():
    ascii_banner = pyfiglet.figlet_format("Hello!!,      Please enter your credentials")
    printy(ascii_banner, "yB" )
    email = input("YOUR EMAIL:")
    passwd = input("YOUR PASSWORD:")
    login(email, passwd)
    ascii_banner = pyfiglet.figlet_format("Successfully logged in, Script is now running")
    printy(ascii_banner, "nB" )
    message = input("Your message that you want to auto reply")
    sendMessage(message)


if __name__ == '__main__':
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    main()