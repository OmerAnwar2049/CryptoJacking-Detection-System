from selenium import webdriver
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller
import urllib.request

# Returns in key value paairs the javascript on a given web page
def get_Javascript(url):
    chromedriver_autoinstaller.install()
    # WEBDRIVER_PATH = 'C:\Windows\chromedriver'
    driver = webdriver.Chrome()
    URL = url
    driver.get(URL)
    scripts = driver.find_elements(By.TAG_NAME, "script")

    sources = {}
    sources["Embedded JS"] = ""
    for script in scripts:
        sources[script.get_attribute("src")] = ""

        # check for embedded javascript
        if script.get_attribute("innerHTML") != "":
            sources["Embedded JS"] += script.get_attribute("innerHTML")
            

    for source in sources.keys():
        url = source
        if url == '' or url == "Embedded JS":
            continue
        try:
            response = urllib.request.urlopen(url)
            sources[source] = response.read().decode('utf-8')
        except:
            print("Error: " + url)
            continue

    driver.quit()
    return sources
