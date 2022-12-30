from turtle import delay

from selenium.common import TimeoutException

from keys.xpath_keys import *
from time import sleep
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys



def get_chromedriver(use_proxy=False, user_agent=None):
    chrome_options = webdriver.ChromeOptions()
    if use_proxy:
        plugin_file = ''

    if user_agent:
        chrome_options.add_argument(f'--user-agent={user_agent}')

    # chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
    service = Service(executable_path=".chromedriver")
    driver = webdriver.Chrome(options=chrome_options, service=service)
    return driver

def login():
    try:
        # user_agent = UserAgent()
        # user_agent.update()
        driver = get_chromedriver()
        driver.maximize_window()
        driver.get("https://visa.vfsglobal.com/tur/en/pol/login")
        # driver.get('https://pr-cy.ru/browser-details/')
        # driver.delete_all_cookies()
        # sleep(15)
        WebDriverWait(driver, delay).until(EC.element_to_be_clickable((By.XPATH, x))).click()
        WebDriverWait(driver, delay).until(EC.element_to_be_clickable((By.ID, gmail))).send_keys("zafardavlatov2003@gmail.com")
        WebDriverWait(driver, delay).until(EC.element_to_be_clickable((By.ID, password))).send_keys('Davlatov3107!')
        # WebDriverWait(driver, delay).until(EC.element_to_be_clickable((By.XPATH, sign_in))).click()
        # WebDriverWait(driver, delay).until(EC.element_to_be_clickable((By.XPATH, important))).click()
        # element = driver.find_element(By.XPATH, important)
        # driver.execute_script("arguments[0].click();", element)



        sleep(20)

        ##########################################
        # Click to the Recaptcha button and solve
        ##########################################

        WebDriverWait(driver, 20).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR,
                                                                                   "iframe[title='reCAPTCHA']")))  # Write the title of the iframe that it is in. Because ReCaptcha checkbox is within an <iframe>
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "div.recaptcha-checkbox-border"))).click()
        print('''
        ##########################################
        # Click to the Recaptcha button and solve
        ##########################################''')

        # The user will manually solve Recaptcha here. Then, the code below will click on Sign In
        sleep(12)  # Recaptcha can be easily solved within 12 seconds

        driver.switch_to.default_content()  # To be able to switch between different Frames
        WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                                                    "button.mat-focus-indicator.btn.mat-btn-lg.btn-block.btn-brand-orange.mat-stroked-button.mat-button-base"))).click()

        ##########################
        # Schedule an appointment
        ##########################

        # If there is no slot for Istanbul region, return back to Dashboard; then try again (to be able to stay in the system)
        for i in range(10000000000):  # We will check for 10000000000 times. This number is enough for 1 day
            try:
                #####################
                # Confirmations page
                #####################
                sleep(12)  # Based on my experiments, 12 seconds should be enough

                WebDriverWait(driver, 20).until(
                    EC.element_to_be_clickable((By.XPATH, "//div[contains(.//text(),'before scheduling')]"))).click()
                WebDriverWait(driver, 20).until(
                    EC.element_to_be_clickable((By.XPATH, "//div[contains(.//text(), 'choose the correct' )]"))).click()

                driver.set_window_size(100,
                                       700)  # When the page is narrowed by the sides, the location of the button is changing and finally the click operation works
                WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                                                            "button.mat-focus-indicator.btn.mat-btn-lg.btn-block.btn-brand-orange.mat-raised-button.mat-button-base"))).click()  # Button class içindeki yazıyı, boşlukları noktalarla değiştirerek yaz. Bekleme yapmadan da çalışmadı bu nedense, stackoverflow'da öyle çözmüş biri

                ############################
                # Terms and Conditions page
                ############################
                WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH,
                                                                            "//div[contains(.//text(), 'Continue Terms and Conditions' )]"))).click()  # Tıkladığında, inspect tarafında renklenen kısmın içindeki "id" değerini gir

                WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                                                            "button.mat-focus-indicator.btn.mat-btn-lg.btn-block.btn-brand-orange.mat-stroked-button.mat-button-base"))).click()  # Button class içindeki yazıyı, boşlukları noktalarla değiştirerek yaz. Bekleme yapmadan da çalışmadı bu nedense, stackoverflow'da öyle çözmüş biri

                driver.maximize_window()  # To easily observe the future operations on the page, turn the window into the maximized version

            except TimeoutException:
                WebDriverWait(driver, 20).until(
                    EC.element_to_be_clickable((By.ID, "navbarDropdown"))).click()  # Click on "My Account"
                WebDriverWait(driver, 20).until(
                    EC.element_to_be_clickable((By.CLASS_NAME, "dropdown-item"))).click()  # Click on "Dashboard"

        # action = ActionChains(driver)
        # action.click(on_element=el)
        # action.perform()
        driver.delete_all_cookies()
    except Exception as ex:
        print(ex)

if __name__ == '__main__':
    login()
