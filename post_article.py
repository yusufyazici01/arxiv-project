import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from src.config import Config

def post_article_selenium(article_content):
    driver = webdriver.Chrome()
    
    
    driver.get("https://partners.foreo.com/login")
    time.sleep(2)
    
    username_field = driver.find_element(By.ID, "username")
    password_field = driver.find_element(By.ID, "password")
    
    username_field.send_keys(Config.FOREO_USERNAME)
    password_field.send_keys(Config.FOREO_PASSWORD)
    
    login_button = driver.find_element(By.ID, "login-button")
    login_button.click()
    time.sleep(3)
    
    new_post_button = driver.find_element(By.ID, "new-post")
    new_post_button.click()
    time.sleep(2)
    
    title_field = driver.find_element(By.ID, "post-title")
    body_field = driver.find_element(By.ID, "post-body")
    
    title_field.send_keys("Daily ArXiv CS Summaries")
    body_field.send_keys(article_content)
    
    
    publish_button = driver.find_element(By.ID, "publish-button")
    publish_button.click()
    
    time.sleep(2)
    driver.quit()


def post_article_api(article_content):
    import requests
    
    url = "https://partners.foreo.com/api/posts"
    headers = {
        "Authorization": f"Bearer {Config.FOREO_API_TOKEN}",
        "Content-Type": "application/json"
    }
    data = {
        "title": "Daily ArXiv CS Summaries",
        "content": article_content
    }
    
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 201:
        print("Article posted successfully!")
    else:
        print("Error posting article:", response.text)
