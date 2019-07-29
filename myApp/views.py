from django.shortcuts import render, redirect
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import os, json, getpass, time


def index(request):
    return render(request, 'index.html')


def search(request):
    uEngine = request.POST['engine']
    uWord = request.POST['keyword']
    uCategory = request.POST['category']

    if request.method == 'POST':
        if uEngine == 'google':
            browser = webdriver.Chrome()
            browser.get('https://www.google.com')

            time.sleep(2)
            search = browser.find_element_by_xpath('//*[@id="tsf"]/div[2]/div/div[1]/div/div[1]/input')
            time.sleep(1)
            search.send_keys(uWord)
            search.send_keys(Keys.ENTER)


            if (uCategory == 'all'):
                elem = browser.find_element_by_link_text("All").click()
            if (uCategory == 'news'):
                elem = browser.find_element_by_link_text("News").click()
            if (uCategory == 'videos'):
                elem = browser.find_element_by_link_text("Videos").click()
            if (uCategory == 'images'):
                elem = browser.find_element_by_link_text("Images").click()
            if (uCategory == 'books'):
                elem = browser.find_element_by_link_text("Books").click()

            time.sleep(2)
            browser.quit()
            return redirect('/')
        if uEngine == 'yahoo':
            yahooCheck()
        if uEngine == 'bing':
            bingCheck()
        if uEngine == 'ask':
            askCheck()
        if uEngine == 'aol':
            aolCheck()
    else:
        return redirect('/')

# def googleCheck(request, uCategory):
#     browser.get('https://www.google.com')


#     if (uCategory == 'all'):
#         elem = browser.find_element_by_link_text("All").click()
#     if (uCategory == 'news'):
#         elem = browser.find_element_by_link_text("News").click()
#     if (uCategory == 'videos'):
#         elem = browser.find_element_by_link_text("Videos").click()
#     if (uCategory == 'images'):
#         elem = browser.find_element_by_link_text("Images").click()
#     if (uCategory == 'books'):
#         elem = browser.find_element_by_link_text("Books").click()