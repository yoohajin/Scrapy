import scrapy as scrapy
from scrapy.http import FormRequest
from scrapy.utils.response import open_in_browser

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import os
import wget

class InstaSpiderSpider(scrapy.Spider):
    name = 'insta_spider'
    start_urls = [
        'http://https://www.instagram.com//'
    ]

    def __init__(self):
    # Log In to your Instagram Account
        driver = webdriver.Chrome('/Users/user/Downloads/chromedriver')
        driver.get('https://www.instagram.com/')
        # Username and Password
        username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                                                               "input[name='username']")))
        password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                                                               "input[name='password']")))

        username.clear()
        password.clear()
        username.send_keys("----")  # username
        password.send_keys("----")  # password

        log_in = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                                                             "button[type='submit']"))).click()
        # remove log in pop-ups
        not_now = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,
                                                                              "//button[contains(text(), 'Not Now')]"))).click()
        not_now2 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,
                                                                               "//button[contains(text(), 'Not Now')]"))).click()

    def parse(self, response):

        # self.driver.get(response.url)
        # res = response.replace(body=self.driver.page_source)
        self.parse(response=self.driver.page_source)
        print(response)
        return response

