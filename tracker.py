import tweepy
import time
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urllib.parse import quote
from pprint import pprint
import os
from dotenv import load_dotenv

load_dotenv()

email = os.getenv('email')
username_tw = os.getenv('username_tw')
password = os.getenv('password')
consumer_key = os.getenv('consumer_key')
consumer_secret = os.getenv('consumer_secret')
access_token = os.getenv('access_token')
access_token_secret = os.getenv('access_token_secret')



chrome_options = Options()
# chrome_options.add_argument("--headless")
chrome_options.add_argument("--incognito")

browser = webdriver.Chrome(options=chrome_options)



auth = tweepy.OAuth1UserHandler(
    consumer_key, consumer_secret, access_token, access_token_secret
)

api = tweepy.API(auth)
# api2 = tweepy.Client(auth2)
user = api.get_user(screen_name="AkhmatovichUz")
# api3.follow_user(target_user_id="AkhmatovichUz", user_auth=True)

while user.followers_count < 10000:
    user = api.get_user(screen_name="AkhmatovichUz")
    print(user.followers_count)
    
if user.followers_count == 9999:
    browser.get(f"https://twitter.com/i/flow/login")
    wait = WebDriverWait(browser, 30)

    element = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "css-1dbjc4n.r-1roi411.r-z2wwpe.r-rs99b7.r-18u37iz")))
    # time.sleep(5)
    login_username = browser.find_element(By.CLASS_NAME, "r-30o5oe.r-1niwhzg.r-17gur6a.r-1yadl64.r-deolkf.r-homxoj.r-poiln3.r-7cikom.r-1ny4l3l.r-t60dpp.r-1dz5y72.r-fdjqy7.r-13qz1uu")
    login_username.send_keys(email)
    time.sleep(2)
    next_button = browser.find_element(By.CLASS_NAME, "css-18t94o4.css-1dbjc4n.r-sdzlij.r-1phboty.r-rs99b7.r-ywje51.r-usiww2.r-2yi16.r-1qi8awa.r-1ny4l3l.r-ymttw5.r-o7ynqc.r-6416eg.r-lrvibr.r-13qz1uu")
    next_button.click()
    
    time.sleep(3)
    
    check = browser.find_element(By.CLASS_NAME, "r-30o5oe.r-1niwhzg.r-17gur6a.r-1yadl64.r-deolkf.r-homxoj.r-poiln3.r-7cikom.r-1ny4l3l.r-t60dpp.r-1dz5y72.r-fdjqy7.r-13qz1uu")
    
    if check:
        check.send_keys(f"{username_tw}")
        next_button2 = browser.find_element(By.CLASS_NAME, "css-18t94o4.css-1dbjc4n.r-sdzlij.r-1phboty.r-rs99b7.r-19yznuf.r-64el8z.r-1ny4l3l.r-1dye5f7.r-o7ynqc.r-6416eg.r-lrvibr")
        next_button2.click()
        time.sleep(5)
        
    password_area = browser.find_element(By.CLASS_NAME, "r-30o5oe.r-1niwhzg.r-17gur6a.r-1yadl64.r-deolkf.r-homxoj.r-poiln3.r-7cikom.r-1ny4l3l.r-t60dpp.r-1dz5y72.r-fdjqy7.r-13qz1uu")
    password_area.send_keys(password)
    time.sleep(2)
    login_button = browser.find_element(By.CLASS_NAME, "css-18t94o4.css-1dbjc4n.r-sdzlij.r-1phboty.r-rs99b7.r-19yznuf.r-64el8z.r-1ny4l3l.r-1dye5f7.r-o7ynqc.r-6416eg.r-lrvibr")
    login_button.click()
    
    time.sleep(5)
    
    browser.get("https://twitter.com/AkhmatovichUz")
    follow_button = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "css-18t94o4.css-1dbjc4n.r-42olwf.r-sdzlij.r-1phboty.r-rs99b7.r-2yi16.r-1qi8awa.r-1ny4l3l.r-ymttw5.r-o7ynqc.r-6416eg.r-lrvibr")))
    browser.save_screenshot("before_ss.png")
    
    time.sleep(5)
    #  = browser.find_element(By.CLASS_NAME, "css-18t94o4.css-1dbjc4n.r-42olwf.r-sdzlij.r-1phboty.r-rs99b7.r-15ysp7h.r-4wgw6l.r-1ny4l3l.r-ymttw5.r-o7ynqc.r-6416eg.r-lrvibr")
    follow_button.click()
    browser.save_screenshot("after_ss.png")
    
 