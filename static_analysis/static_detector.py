from selenium import webdriver
from selenium.webdriver.common.by import By
import urllib.request
# import yara
import chromedriver_autoinstaller
from urlFetcher import *

class Static_Detector:

    def __init__(self) :
        
        self.url_Fetcher = Url_Fetcher()
        self.urls = {}    ## For storing urls
        self.analysis = {}   ## For storing final verdicts

    def getValues(self,url):
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

    def statrtMonitor(self):

        while(1):
            url = self.url_Fetcher.getSingleUrl()
            if url != "-1":
                self.urls[url] = 1
                values = self.getValues(url)
                print(values)
            sleep(5)
            print("Waiting")


s_monitor = Static_Detector()

print(s_monitor.statrtMonitor())

            
            
