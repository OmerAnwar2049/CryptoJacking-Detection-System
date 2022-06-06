from selenium import webdriver
from selenium.webdriver.common.by import By
import urllib.request


# def get_url(url):
#     WEBDRIVER_PATH = 'C:\Windows\chromedriver'
#     driver = webdriver.Chrome(WEBDRIVER_PATH)
#     # URL = url
#     # driver.get(URL)
#     # scripts = driver.find_elements(By.TAG_NAME, "script")

#     # sources = {}
#     # for script in scripts:
#     #     sources[script.get_attribute("src")] = ""

#     # for source in sources.keys():
#     #     url = source
#     #     file = urllib.request.urlopen(url)
#     #     sources[source] = file.read().decode('utf-8')
#     #     # print(sources[source])
#     #     # print()
#     # driver.quit()
#     # return sources
#     return []


# values = get_url(
#     "http://127.0.0.1:3000/miner/index.html")
# for value in values.keys():
#     print(value)
#     # print()

rules = yara.compile(filepath='./rules.yara')
a = "This is my malicious string hash"

matches = rules.match(data = a)

print(matches)